# Machine Learning

+ Supervised Learning
  + Examples of I/O pairs
+ Unsupervised Learning
  + Only given inputs
+ Reinforcement Learning
  + Examples given one by one
  + Guess to gain reward, try to get max reward

## Environment types

+ passive and deterministic
+ passive and stochastic
+ active and det
+ act and sto

## Reinforcement Learning

+ Tries to find the best way to act in uncertain and non-deterministic environment
+ Aim to find policy $\pi:S\rArr A$ that maximise reward 

### BOXES algorithm

+ each box contains statistics on performence of controller, updated on each failure
  + How many times each action is performed
  + Sum of length of time system survived after taking particular action

#### Exploration and Exploitation

+ Some times not to choose best action
+ if $\frac{LeftLife}{LeftUsage^k}>\frac{RightLife}{RightUsage^k}$
  + k is a bias to force exploration
  + e.g. k = 1.4
  + When usage of an action grows much more than that of another, algorithm will switch and do some exploration
+ Boltzmann equation


#### Performance

+ Fast
+ Only work for episodic problems
  + has specific termination
+ Doesn't work for continuous problems
  + like Stumpy

#### State transition Graph

+ Each node is a state
+ Action cause transition
+ Policy is the set of transition rules
  + Which action in given state
+ Receive reward after action
+ May non-det

## Markov Decision Process

+ Assume current state is enought to make a decision
+ Assume action are assumed to have fixed duration
+ What is it?

### Expected Reward

+ $V^\pi(S_t)=\sum^\infin_{i=0}\gamma^ir_{t+i}$
  + $\gamma$ is discount factor
  + V is the expected value of following $\pi$
  + $V^\star$: optimal policy
+ Value for a state

### Q Value

+ $Q(s,a)=r(s,a)+\gamma V^*(s')$
+ Value for an action

#### Q Learning

+ initialise $Q = \{0\}$
  + $Q(s,a)=r+max Q(s', a')$
  + s=s'
  + Repeat
