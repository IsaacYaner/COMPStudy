# Spec Ass 1

## Elements

+ Counter $c$
  + $1$ writer
    + Increment $c$ by one and $mod$
  + $R$ reader
    + Read $c$ byte by byte as $v$
    + $v$ is correct when $v=c$
  + $B$ bytes
    + c:$[0...2^{8B-1}]$
+ Only w/r bytes is atomic

## Submission

+ Report - **counter.pdf**
  + Assumption
  + Reasoning
+ Java implementation - **Counter.java**
  + using **Thread** onlys
+ Promela encoding - **counter.pml**
  + of algorithm
  + of requirements
+ **partner.txt**
  + zID of partner

`give cs3151 assn1 Counter.java counter.pml counter.pdf partner.txt`

## Java

+ **3** args    
  + $R, B, k$
  + $k$ is rounds of process to be performed by each process
    + $k=0$ Loop indefinitely
+ One thread per process
+ **No** promitives
  + **can** use *volatile*
+ **Cannot** use timer/sleep

## Promela

+ **Two** #define
  + for $R, B$
+ Verify for small values
+ Verify for $k=0$

## Report

+ Summary
+ Explain algorithm
+ Highlights
  + limitations/solutions
+ Reproduce guideline
+ Name&ID



flag 1 = false
read byte 1
Check flag 1
read byte 2
flag 2 = false
flag 2 = true
flag 2 = false
flag 2 = true
flag 2 = false
flag 2 = true
flag 2 = false
flag 2 = true
flag 2 = false
flag 2 = true
flag 2 = false
flag 2 = true
Check flag 2
