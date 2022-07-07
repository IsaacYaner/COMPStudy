# Week 1

+ Email
  + cs3151@cse.unsw.edu.au

## Set and behaviour

+ Behaviour is a infinite sequence of states
+ Property is a set of behaviours
+ $[P]\subseteq A$

## State

+ Internal state
  + Stuttering is repeating visually equivalent state
+ External state

## Property

+ Set of behaviours
+ Safety property
  + something bad will never happen
  + may be violated by a finite prefix of a behaviour 不用检测所有的情况就可以知晓，这个property不hold
  + Limit closed
  + s永远不出现，如果s出现在$\bar A$了，那么一定会出现在$A$
+ liveness property
  + something good will happen
  + You can't examine a finite state to get a result
  + dense set
  + s总会出现，任何sequence加上一个包含s的behaviour都在$A$里面

### Alpern and Schneider's Theorem

+ Every property is the intersection of safety and liveness
+ $P = \bar P \bigcap \Sigma^\omega \backslash(\bar P\backslash P)$

## Limit

+ $b|_k$ means first k states of behaviour.

### Limit closure

+ All the behaviours that take first n states, there is always at least one existing in A
  + Usually $A\subseteq \bar A$
+ s in closure of A if any prefix of s is in A
+ Limit closed $A= \bar A$
  + limit closure is already limit closed
+ dense:
  + $\bar A = \Sigma^\omega$
+ Limit closure of empty is also empty
