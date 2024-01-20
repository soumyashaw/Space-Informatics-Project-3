# Task 2 - Scheduling

## Decision variables

<!-- Please explain your decision variables here: What do they mean, why do you model them like that, ... -->

We need $n$ decision variables, representing $n$ time stamps.

## Objective function

<!-- Please explain your objective function here: What you want to optimize for, why you need which variables for it, ... -->

We want to achieve nothing, hence we minimize the simple sum of our decision variables, hoping it will be close to 0.

$$
\text{minimise} \quad \sum x_i
$$

## Constraints

<!-- Please explain your constraints here: Why are they necessary, what do they represent, ... -->

All decision variables with an even index must be strictly positive.

$$
\forall x_i.\; i \bmod 2 = 0 \implies x_i > 0
$$

All decision variables with an odd index must be strictly negative.

$$
\forall x_i.\; i \bmod 2 = 1 \implies x_i < 0
$$

## Synchronization Delay

<!-- Please describe your example here when a solution considering synchronization delay differs from one that does not consider it. -->
