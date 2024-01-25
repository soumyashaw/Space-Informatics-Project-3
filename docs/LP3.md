# Task 3 - Keeping an Eye on the battery

## Decision variables

<!-- Please explain your decision variables here: What do they mean, why do you model them like that, ... -->

Similar to the previous approach, we choose $x$ and $y$ as our decision variables, where $x$ represents the scheduling of the time interval for the Moon Colony A and $y$ represents the scheduling of the time interval for the Moon Colony B.

The variables are binary and represent the following:

$x[i] = 1$ if the time interval is allocated to Moon Colony A for communication. 
$x[i] = 0$ if the time interval is not allocated to Moon Colony A for communication. (i.e. it does not communicate)

$y[i] = 1$ if the time interval is allocated to Moon Colony B for communication.
$y[i] = 0$ if the time interval is not allocated to Moon Colony B for communication. (i.e. it does not communicate)

## Objective function

<!-- Please explain your objective function here: What you want to optimize for, why you need which variables for it, ... -->

Similarly, we maximize the data transfer between the satellite and the Moon Colonies. Hence, we chose to maximize the sum of the decision variables multiplied by the Data Transfer in the given Intervals.


$$
\text{maximise} X * D_A + Y * D_B
$$

where $D_A$ is the data transfer for Moon Colony A and $D_B$ is the data transfer for Moon Colony B.

## Constraints

<!-- Please explain your constraints here: Why are they necessary, what do they represent, ... -->

The first constraint is that the scheduling must obey the fairness constraint:

$$
| X * D_A - Y * D_B | \le \epsilon
$$

The next constraint is that the scheduling must ensure only one Moon Colony is communicating at a time. At the same time, it should also allow no scheduling at all (i.e. No Colony is communicating). Hence, we chose to add the following constraint:

$$
x[i] + y[i] \le 1
$$

The last and the most important constraint is that the scheduling must ensure that the battery does not go below the threshold. We feel this contraint makes the problem more complex and hence, we tried to simplify the problem further by enforcing a simple case. We know that the discharging rate is much higher than the harging rate and it will take time for the battery to charge. Hence, we mandated the scheduler to charge the battery whenever sunlight was available. This simple case removed another variable for computation. For that, we trim the colony access times according to the sunlight access times.

Now, to take care of the battery, we we deed to iterate over the colony access times and further iterate over all intervals that come before it to check if the battery is charged enough to communicate with the colony. So, 

$$
totalTimeDischarging = \sum_{i=0}^{n-1} x[i] * y[i] * intervalTime[i]
totalTimeCharging = \sum_{i=0}^{n-1} sunIntervalTime[i]
$$
where $n$ is the index of current node

We calculate the predicted battery level at the end of the current interval and add it to the $totalTimeDicharging$. We calculate the $soc_t = max(0, min(soc_0 - (totalTimeDischarging * l_d + totalTimeCharging * l_t, 1))$ where $soc_0$ is the initial battery level. We also add the charging time to the $totalTimeCharging$. We finally add the contraint $soc_t \ge threshold$ for each iteration.





