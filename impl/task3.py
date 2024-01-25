import gurobipy as gp
from gurobipy import GRB

from spain import namespace
from spain.types import IntervalList
from spain.util import parse_stk_date, collected_data

__all__ = [
    "find_schedule_with_battery_lp",
]

def mergeIntervals(listA, listB):
    """Given two lists of intervals, the function merges them into one list of intervals.
    In case of overlapping intervals, the function chooses the interval with the maximum 
    duration (max data collected)."""
    mergedIntervals = []

    allIntervals = listA + listB
    
    allIntervals.sort(key=lambda x: x[0])
    
    currentInterval = allIntervals[0]
    
    for interval in allIntervals[1:]:
        if interval[0] <= currentInterval[1]:
            if (interval[1] - interval[0]) > (currentInterval[1] - currentInterval[0]):
                currentInterval = interval
        else:
            mergedIntervals.append(currentInterval)
            currentInterval = interval
    
    mergedIntervals.append(currentInterval)
    
    return mergedIntervals

def findCoincidingIntervals(listA, listB):
    """Given two lists of intervals, the function finds the coinciding intervals between the two lists."""
    coincidingIntervals = []

    # Combine both lists
    allIntervals = listA + listB
    
    # Sort intervals based on start time
    allIntervals.sort(key=lambda x: x[0])

    for i in range(1, len(allIntervals)):
        if allIntervals[i][0] <= allIntervals[i - 1][1]:
            # Coinciding intervals found
            coincidingIntervals.append((max(allIntervals[i][0], allIntervals[i - 1][0]), min(allIntervals[i][1], allIntervals[i - 1][1])))

    return coincidingIntervals

def findMutuallyExclusiveIntervals(listA, listB):
    """Given two lists of intervals, the function finds the mutually exclusive intervals between the two lists.
    The function keeps the first interval list intact and trims the second interval list if needed."""
    resultIntervals = []

    # Combine both lists
    allIntervals = sorted(listA + listB, key=lambda x: x[0])

    currentInterval = allIntervals[0]

    for interval in allIntervals[1:]:
        if interval[0] > currentInterval[1]:  # Non-overlapping intervals
            resultIntervals.append(currentInterval)
            currentInterval = interval
        else:
            # Trim the second interval if needed
            currentInterval = (currentInterval[0], max(currentInterval[1], interval[1]))

    resultIntervals.append(currentInterval)

    return resultIntervals

def getSocAfterUsage(currentSoc, timeDuration, load, capacity = 100.0):
    """Given the current state of charge, the function calculates the state of charge after the usage."""
    soc = max(0, min(currentSoc - (timeDuration * load), capacity))
    return soc

def calculateBatteryUsage(m, timeInterval, index, varX, varY):
    totalDischargeTime = 0.0
    totalChargeTime = 0.0

    for itr in range(index):
        totalDischargeTime += varX[itr] * varY[itr] * mergedIntervalsTime[itr]

    for itr in range(len(sunIntervalsTime)):
        if sunIntervals[itr][0] < timeInterval[0]:
            totalChargeTime += sunIntervalsTime[itr]

    print(mergedIntervalsTime[index], (timeInterval[1] - timeInterval[0]).total_seconds())

    totalDischargeTime += mergedIntervalsTime[index]

    m.addConstrs(namespace.initial - (totalDischargeTime * namespace.load.discharge_rate) + (totalChargeTime * namespace.load.charge_rate) >= namespace.charge, "battery_constraint")



def find_schedule_with_battery_lp(
    m: gp.Model,
    access_A: IntervalList,
    access_B: IntervalList,
    access_sun: IntervalList,
) -> tuple[IntervalList, IntervalList, IntervalList]:
    """Find an optimal schedule for the Moon satellite to connect to both colonies fairly using linear programming while not depleting the battery."""

    intervals_A: IntervalList = []
    intervals_B: IntervalList = []

    global mergedIntervalsTime, sunIntervalsTime, sunIntervals

    intervals_sun: IntervalList = []
    sunIntervals = access_sun

    # Compute battery-aware schedule
    # Merge the intervals of the two colonies into coinciding intervals
    mergedIntervals = findCoincidingIntervals(access_A, access_B)

    # Merge the coinciding intervals with the sun intervals into mutually exclusive intervals
    mergedIntervals = findMutuallyExclusiveIntervals(access_sun, mergedIntervals)

    # Sort the intervals based on start time
    mergedIntervals.sort(key=lambda x: x[0])
    
    sunIntervalsTime = []
    for itr in access_sun:
        # Caluculate the Time Duration (sec) in the interval
        sunIntervalsTime.append((itr[1] - itr[0]).total_seconds())

    mergedIntervalsTime = []
    for itr in mergedIntervals:
        # Caluculate the Time Duration (sec) in the interval
        mergedIntervalsTime.append((itr[1] - itr[0]).total_seconds())

    mergedIntervalsData = []
    for itr in mergedIntervals:
        # Caluculate the Data collected in the interval
        mergedIntervalsData.append(collected_data(itr[0], itr[1]))

    x = range(len(mergedIntervalsData))
    y = range(len(mergedIntervalsData))
    
    x = m.addVars(x, vtype=GRB.BINARY, name="x")
    y = m.addVars(y, vtype=GRB.BINARY, name="y")

    m.setObjective(x.prod(mergedIntervalsData) + y.prod(mergedIntervalsData), GRB.MAXIMIZE)

    m.addConstr(x.prod(mergedIntervalsData) - y.prod(mergedIntervalsData) <= namespace.epsilon, "fairness_constraint")
    m.addConstr(y.prod(mergedIntervalsData) - x.prod(mergedIntervalsData) <= namespace.epsilon, "fairness_constraint_2")

    m.addConstrs(x[i] + y[i] <= 1 for i in range(len(mergedIntervalsData)))

    for i in range(len(mergedIntervalsTime)):
        socPredicted = calculateBatteryUsage(m, mergedIntervals[i], i, x, y)
        #m.addConstr(socPredicted >= namespace.charge, "battery_constraint")

    m.optimize()

    solvedX = [int(var.x) for var in list(x.values())]
    solvedY = [int(var.x) for var in list(y.values())]

    for itr in range(len(solvedX)):
        print(solvedX[itr], solvedY[itr])

    return intervals_A, intervals_B, intervals_sun
