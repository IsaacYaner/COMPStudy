# Signal Passing

## Basics

+ Send
  + ch **!** x
    + FIFO
  + ch **!!** x
    + Sort x into the queue
+ Receive
  + ch **?** x
    + FIFO
  + ch **?** \<x>
    + read only, doesn't pop
  + ch **??** x
    + Pop first one that matches pattern
  + ch **??** \<x>

## Communication

+ Syntax matching
+ Semantically matching

### Simplistic method

+ make local assertion network
+ show internal transition
+ show matching pairs
+ Drawbacks
  + But no guarantee on interfering freedom because no shared variable
  + Sound but not complete

### Levin Gries

+ Shared variable

### AFR

+ Not shared variable, but communication invariant $I$
