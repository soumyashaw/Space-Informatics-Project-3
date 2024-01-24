import gurobipy as gp
from gurobipy import GRB

from spain import namespace
from spain.types import IntervalList
from spain.util import parse_stk_date, collected_data

__all__ = [
    "find_schedule_lp",
]

def mergeIntervals(listA, listB):
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



def find_schedule_lp(
    m: gp.Model, access_A: IntervalList, access_B: IntervalList, *args
) -> tuple[IntervalList, IntervalList, None]:
    """Find an optimal schedule for the Moon satellite to connect to both colonies fairly using linear programming."""

    intervals_A: IntervalList = []
    intervals_B: IntervalList = []

    # Compute schedule
    mergedIntervals = mergeIntervals(access_A, access_B)
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

    m.optimize()

    solvedX = [int(var.x) for var in list(x.values())]
    solvedY = [int(var.x) for var in list(y.values())]

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
