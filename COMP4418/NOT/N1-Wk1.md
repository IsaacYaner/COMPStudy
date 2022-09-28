# Wk1

## Rule set 

$P=\{r,r,r\}$
$r=Head(r)\leftarrow Body(r)$

## Stable model

**Minimal** set that satisfies all rules

**Reduct $P^S$**: Delete all negated atoms in the body

### How to get

+ Start from empty
+ add true statements
+ Until nothing to add

**S** is stable model of **P** iff **S** is a stable model of $P^S$

## Question

+ Reduction?????
