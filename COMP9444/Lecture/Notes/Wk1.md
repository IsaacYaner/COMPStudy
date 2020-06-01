# Wk1

## Perceptron

+ Machine that simulate human brain to recognise object and difference
+ Can only compute **linearly separable functions**
+ Has credit assignment problem

### neuron

function|Input|threshold|output|connection
-|-|-|-|-
Neuron|dendrite|soma|axon|synapse
Node|Input edges|transfer function|output edges|weight
symbols|$\bar x$|g(f($\bar x$))||$\bar w$

+ **Activation level**
  + $s=f(\bar{x})$
  + $\sum_{i=0}^n w_ix_i$
  + $w_0 = threshold, x_0 = 1$
    + **Bias**
      + bias comes from +/- properties of threhold
      + Positive threshold->hard to fire
      + vice versa
+ **Transfer function**
  + $g(s)$

#### Examples

Function|$w_1$|$w_2$|$w_0$
-|-|-|-
 **AND**|1|1|-1.5 
 **OR**|1|1|-0.5
 **NOR**|-1|-1|0.5
+ NOR = NOT OR
  + thus $f_{NOR} = -f_{OR}$

#### Learning Process

+ Adjust $w$ and threshold $w_0$ by $\eta>0$
+ When $g<required$
  + for $w_i$ : $\bar w$
      + $w_i+=\eta x_i$
  + Effect: $s+=\eta(\sum(x_i^2))$
+ Vice versa

## Backpropagation
