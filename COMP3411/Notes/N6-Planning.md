# Planning

+ Reasoning about action
+ STRIPS Planner
+ Forward planning 
+ Regression Planning
+ Partial Order Planning
+ GraphPlan
+ Planning as Constraint Satisfaction

## Agent acting in its environment

+ Agent
  + Competences Goals
  + Preferences Initial knowledge
+ Observe environment, get perceptions
+ Give asctions with planning

## Planning

+ Deciding what to do based on agent's ability, goals and state of the world
+ Find a sequence of action to solve a goal
+ Assumptions
  + World is deterministic
  + No exogenous events outside of control of robot change state of the world
  + The agent Knows what state it is in
  + Time progresses discretely from one state to the next
  + Goals are predicates of states that need to be achieved or maintained

### Planning Agent

+ More flexible than reactive agent because knowledge to support decisions is represented  explicitly and can be modified
+ Behaviour can be easily changed
+ Doesn't work when assumptions are violated
+ Actions change environment
+ Planning scenario
  + Agent can control its environment
  + Only atomic actions, not processes with duration
  + Only single agent in the enviroment (no interference)
  + Only changes dur to agent executing actions (no evolution)
+ Examples
  + Robo soccer
  + Delivery robot
  + Self-driving car

## Representations

+ Planning problem
  + States
  + Actions
  + Goals
+ Relation between states and actions
  + Explicit state space representation
  + action-centric
  + feature based

### Actions

+ Deterministic action : is a partial function from states to states
+ Preconditions of an action : specify when the action can be carried out
+ Effect : resulting state

#### Explicit state space representation

+ Usually too many states to represent
  + to acquire and to reason with
+ Small changes to the model change largely to the representation
  + Adding a feature changes the whole representation
+ Doesn't represent the structure of states

#### STRIPS Language

+ Stanford Research Institute Problem Solver
+ Simplifications
  + No variables in goals
  + Positive relations given only
  + Unmentioned relations are assumed false
  + Effects are conjunctions of relations
+ Each action has a
  + Precondition
  + effect : a set of assignments of values to primitive features made by this action
    + Often split into an ADD list (things that become true after action)
    + and DELETE list (become false after)
    + Assumption not mentioned unaffected

#### Feature based representation of actions

+ **Precondition**: proposition specifies when the action can be carried
+ **Casual rules**: when the feature gets a new value
+ **Frame rules**: when the feature keeps its value

### Relational State representation

#### Defining Goals and Possible actions

#### STRIPS actrion schema

+ **Action schema**: a set of action using variables
  + Shows
    + Action
    + Precondition
    + Adds
    + Deletes
    + Additional constraints

### PDDL

+ Planning Domain Description Language
+ Extension of STRIPS
+ For planning competitions to provide an implementation independent language for describing action schema and domain knowledge
+ Variants to cover domains
  + continuous domains, continuous actions, probabilities, etc.

#### Algorithms

+ Forward search
+ goal regression

#### Forward search

+ dNodes are states in the world
+ Arcs corresponds to actions transforming state
+ Start node is initial state
+ Terminate when goal condition is satisfied
+ Path is plan to achieve goal

#### Regression Planning

+ Nodes are subgoals
+ Arc corresponds  to actions
+ Start node is goal
+ $g' = (g-Add(a))UPrecond(a)$

### Sussman's Anomaly

+ C on A, Goal is A on B, B on C
+ Need to move c on floor first

#### WARPLAN

+ Interleave actions by protecting goals
  + If try to undo a protected goal, move backwards and try to slot new plan

### Partially Ordered Plans

+ Some steps are ordered, but no overall order (only necessary actions are ordered)

### Planning Graphs

+ Used constraint solving to better heuristic
+ Only for propositional problems
+ Sequence of levels of when time of the step
  + L0 = ini
  + Each level
    + Set of lietrals, actions
      + Literals that possibily be true, depend on previous step action
      + Actions that possible, depend on literals hold
        + There is inactions
  + Conflict represented by links
  + Until two cons levels are identical
  + Until goal appear

#### Mutual Exclusion

+ Action
  + Inconsistent effects: One action negates an effect of the other
  + Competing needs: Precondition of one is mutually exclusive with that of the other
+ Literals
  + One is negation of the other
  + Inconsistent support: Each possible pair of actions achieve mutually exclusive literals

#### and Heuristic Estimation

+ Planning Graph provide information about the problem
  + Literal not in final level is not achieveable
    + Useful for backward search
  + Level of appearance can estimate cost of achieveing goal = level cost
  + Cost of a conjunction of goals heursitics
    + Max level
    + Sum level
    + Set level

##### RXTRACT_SOLUTION

+ Use Boolean CSP
+ Initial state = last level
+ Action = any set of non-conflicting actions cover goal
+ Goal = reach S0
+ Cost = 1 each action
+ Terminating

##### Extracting the plan

+ Heuristic forward use A*
  + Cost based on level in graph

## Question

+ What is interference in p.48?
