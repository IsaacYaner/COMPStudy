# Week 3

## Invariant

+ **OG** (Owicki-Gries)
  + annotate each location with invariant
  + show that assertion is inductive
  + show interference freedom

## More liveness Desiderata

+ Eventual Entry
  + $\square wait\Rightarrow \diamond enter$
+ Bounded waiting
  + Pre-protocol can be bypassed at most n times (Non-Linear property)
  + Bounded Eventual entry
+ Linear waiting
  + No process can enter cs twice while another preing (linear)

## Tie-Breaker (Peterson's) algorithm

+ Lock&Last
  + await unlock and last is not me
  + First one wants to enter is trapped
    + The other one unlock the trap after cs
+ Generalised
  + in[]
    + Which trap i is in 
  + last[]
    + process id of trap j
+ Doesn't satisfy contrainted waiting property

## Simplified Bakery algorithm

+ Use a counter to store ticket number
+ Hard to verify using SPIN
+ Generalised

### Lamport's Bakery algorithm

+ Use choosing and number
+ Wait for all other to choose
  + And then wait for your turn
+ Preprotocol O(n), and number may exceed

+ Fast algorithm
  + O(1) accesss to cs with no waits
  + Sacrifice eventual entry

## Lamport's Fast algorithm

+ Two gates
  + set gate1 directly
  + Proceed only when gate2 is blank
+ If name on any gate, goto cs
+ Set gate2 blank afterwards

### Modification

+ add wantp and wantq

### Generalisation

## Problem Review

+ Peterson with square complexity
+ Some reply on xc\ts instructions
+ Bakery uses unbounded ticket numbers
+ Fast sacrifices eventual entry

## Szymanski's

+ Linear wait
+ No problems
+ Waiting room
  + Gather one wave, and another
  + Anyone can close the door
    + Close the door when noone wants to enter
    + Usually the last one that wants to enter

## Machine instructions

+ xc
+ ts
  + read from share and set share to 1
+ Lock
+ Test and test and set
