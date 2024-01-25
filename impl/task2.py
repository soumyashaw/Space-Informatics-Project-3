# Imports
import gurobipy as gp
from gurobipy import GRB

from spain import namespace
from spain.types import IntervalList
from spain.util import parse_stk_date, collected_data

__all__ = [
    "find_schedule_lp",
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


def find_schedule_lp(
    m: gp.Model, access_A: IntervalList, access_B: IntervalList, *args
) -> tuple[IntervalList, IntervalList, None]:
    """Find an optimal schedule for the Moon satellite to connect to both colonies fairly using linear programming."""

    intervals_A: IntervalList = []
    intervals_B: IntervalList = []

    # Compute schedule
    # Find the coinciding intervals between the two lists where scheduling can be chosen among the two.
    mergedIntervals = findCoincidingIntervals(access_A, access_B)
    mergedIntervalsData = []

    # Iterate through the merged intervals and calculate the data collected in each interval
    for itr in mergedIntervals:
        # Caluculate the Data collected in the interval
        mergedIntervalsData.append(collected_data(itr[0], itr[1]))

    # Create a new model
    x = range(len(mergedIntervalsData))
    y = range(len(mergedIntervalsData))

    # Create variables for the model. x represents the intervals chosen for colony A 
    # and y represents the intervals chosen for colony B. Both are binary variables to represent scheduling.
    # x[i] = 1 represents that the ith interval is allocated to colony A for communication.
    # y[i] = 1 represents that the ith interval is allocated to colony B for communication.
    # 0 in both variables represents that the interval is not allocated to the colony. (i.e. no communication)
    x = m.addVars(x, vtype=GRB.BINARY, name="x")
    y = m.addVars(y, vtype=GRB.BINARY, name="y")

    # Set objective function
    # To maximize the data collection
    m.setObjective(x.prod(mergedIntervalsData) + y.prod(mergedIntervalsData), GRB.MAXIMIZE)

    # Add constraints (fairness constraint)
    m.addConstr(x.prod(mergedIntervalsData) - y.prod(mergedIntervalsData) <= namespace.epsilon, "fairness_constraint")
    m.addConstr(y.prod(mergedIntervalsData) - x.prod(mergedIntervalsData) <= namespace.epsilon, "fairness_constraint_2")

    # Add constraints (scheduling constraint)
    # i.e. if an interval is chosen for colony A, it cannot be chosen for colony B and vice versa.
    # However, both can remain 0 as well denoting no communication.
    m.addConstrs(x[i] + y[i] <= 1 for i in range(len(mergedIntervalsData)))

    m.optimize()

    # Retrieve the solved values for x and y
    solvedX = [int(var.x) for var in list(x.values())]
    solvedY = [int(var.x) for var in list(y.values())]

    # Iterate through the solved values and append the intervals to the respective lists
    for itr in range(len(solvedX)):
        if solvedX[itr] == 1:
            intervals_A.append(mergedIntervals[itr])
        if solvedY[itr] == 1:
            intervals_B.append(mergedIntervals[itr])

    return (
        intervals_A,
        intervals_B,
        None,
    )  # None required to achieve same signature as task 3
