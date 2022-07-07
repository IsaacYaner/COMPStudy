# Semaphore

+ $(v,L)$
  + v: number of accessable processes
  + L: List of processes
+ wait() P()
  + execute
+ signal() V()
  + Unblock a process in L or add V

## Categories

+ Busi-wait semaphore
  + very weak
  + Processes call wait by them selves
  + The one who is lucky get the ticket
+ Weak semaphore
  + Don't have to retry wait
+ Strong semaphore 
  + FIFO
  + Don't need to retry wait

## Signaling disciplines

+ Hoare's "Immediate resumption requirement"
  + $E<S<W$
+ Java
  + $E=W<S$

## Simulate Promela

+ 
