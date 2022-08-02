# Termination

## Termination

+ Convergence + Deadlock-free
+ $\phi$-convergent
  + Converge happens if initial state satisfies $\phi$

## Wellfounded set

+ Partial order
  + Irreflexive
    + $a\nprec a$
  + Asymmetric
    + $a\prec b \Rightarrow b\nprec a$
  + Transitive
    + $a\prec b \wedge b\prec c\Rightarrow a\prec c$
+ Wellfounded
  + every descending sequence in partial order is finite

### Floyd's Wellfoundedness Method

+ **Sound**
+ Semantically complete
  + If P is convergence, exist networks
+ Transition diagram $P=(L,T,s,t)$
+ precondition $\phi$
  + Find an inductive assertion network
    + $Q:L\rightarrow (\Sigma\rightarrow \mathbb{B})$
    + $\models\phi\Rightarrow Q_s$
  + Choose a wellfounded set and a network of partial ranking functions
    + from $\Sigma$ to $W$
    + $Q_l$ implies $p_l$
    + every transition decreases ranking function
+ For WFO, ranking function for $\{\mathbb{N}<\}$ is called variant

### Prove

+ Locally consistent
+ Local correctness
+ Interference freedom

### AFR

+ Get AFR and WFO, ranking function
+ Locally consistent
+ Internal ordered
+ ranking coorporate between matching pairs

## Divergence

### Deadlock

+ Not terminated, no transitions available
+ Message deadlock
  + block on channel
+ Resource deadlock
  + guard never become true
+ Avoidance
  + Ordering
  + Banker's Algorithm
    + guarantee entrance: no multiple processes hold partial resources

### Hoare Rule

+ Pipe-dream parallel rule
  + unsound
  + Add more info
    + Side conditions
    + **Rely-guarantee** method (Cliff Jones)
      + Incomplete without auxiliary variables
      + Requirements
        + Precondition
        + Postcondition
        + Rely (Environment not to do)
        + Guarantee (I won't do)
    + Restrict processes

### Synchronous Transition Diagram

+ Processes do not share variables
+ Communicating through channels
  + Unidirectional
  + shared by at most 2

### AFR and  L&G

+ Closed systems
+ Reason the whole system
  + Can't reason **compositionally**
    + infer from constituents without knowing internal structure

#### Compositionally-Inductive Assertion Network

+ $h$ handles all communication history
+ Partial Correctness
  + $P\vdash Q\ |\ \{Q_s\} P \{Q_t\}$
  + Initial empty history
  + Consequence rule
    + Can deduce with stronger pre and weaker post condition

#### Parallel composition rule

+ $\psi_i$ only asserts
  + local variables
  + history directly with $P_i$
+ 

## Question

+ $\Sigma$
+ Types of completeness?
+ Owicki-Gries
+ Interference freedom？
+ Hoare triple
+ Compositionality is a red herring
