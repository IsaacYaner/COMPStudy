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


