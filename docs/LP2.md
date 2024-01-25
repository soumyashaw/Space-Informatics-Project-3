# Task 2 - Scheduling

## Decision variables

<!-- Please explain your decision variables here: What do they mean, why do you model them like that, ... -->

We choose $x$ and $y$ as our decision variables, where $x$ represents the scheduling of the time interval for the Moon Colony A and $y$ represents the scheduling of the time interval for the Moon Colony B.

The variables are binary and represent the following:

$x[i] = 1$ if the time interval is allocated to Moon Colony A for communication. 
$x[i] = 0$ if the time interval is not allocated to Moon Colony A for communication. (i.e. it does not communicate)

$y[i] = 1$ if the time interval is allocated to Moon Colony B for communication.
$y[i] = 0$ if the time interval is not allocated to Moon Colony B for communication. (i.e. it does not communicate)

## Objective function

<!-- Please explain your objective function here: What you want to optimize for, why you need which variables for it, ... -->

We wanted to maximize the data transfer between the satellite and the Moon Colonies. Hence, we chose to maximize the sum of the decision variables multiplied by the Data Transfer in the given Intervals.


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


## Synchronization Delay

<!-- Please describe your example here when a solution considering synchronization delay differs from one that does not consider it. -->
For cases where the access time interval is less than the synchronization delay, the solution considering the synchronization delay will be different from the one that does not consider it.

For example, there might be several time intervals, less than the synchronization delay, which will ignored by the current model. However, the model not considering the synchronization delay will consider these time intervals and allocate them to the Moon Colonies making it easy for maintaining the fairness constraint.


## Motivation for formulation

We particularly went for this formulation of the problem because we wanted to maximize the data transfer and keep the fairness as a constraint rather than a goal.

Since the satellite can communiate with one Moon Colony at a time, we could've taken the initial access intervals into the problem but it also adds another layer of complexity to the problem. The scheduler needs to allocate the communication to that Moon Colony and leaves no room for decision.

Hence, we chose to select only the overlapping intervals to be able to communicate to both Moon Colonies and choose one everytime allowing flexibility to the scheduler and also more probable to comverge to a solution satisfying the fairness constraint.