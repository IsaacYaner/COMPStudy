# Week 2

## LTLs


## Testing

+ For n states and m actions
  + $\frac{(nm)!}{m!^n}$ scenarios
+ Testing method
  + model checking
    + exhaustively find a counterexample
    + Partial order reduction
    + Common way
      + easy to use
      + instructive counter examples
      + *state explosion*
        + COMP3153
        + Spin root
  + theorem proving
    + formal proof
      + No limit on state space
      + *expert users to hand-crack*

## Promela

+ Limited critical reference
  + Each statement only accesses one shared variable at once
+ Ensuring atomicity
  + atomic
  + d_step
    + always ensure the process is finished before the next one (blocks->runtime error)


## Critical section problem

&emsp;critical section: uninterruptable code
+ pre-protocol
  + Critical Section
+ Post-protocol

### Desiderata

&emsp;**safety** *Liveness*
  + **Mutual exclusion**
  + only one critical section can be alive
+ *Eventual entry*
  + Once pre-protocol is executed, critical section will eventually happen
+ Abscence of Deadlock
  + always have process to run
+ Abscence of unnecessary Delay
  + Not prevented before entering critical session

### Approaches

+ one lock variable
+ two lock variables *(Dead lock)*
  + wait another first
  + set this first
    + switch lock while waiting *(Live lock)*
  + Add a **turn** variable, wait for my turn to lock *(wait for turn forever)* **(Dekker's algorithm)**

#### Dekker's algorithm

+ The turn one
+ Introduces fairness assumption
  + If can move, it will eventually move
+ Fairness
  + Weak fairness
    + $\square (\square enabled(\pi) \Rightarrow \diamond taken(\pi))$
  + Strong fairness


