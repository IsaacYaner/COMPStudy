# Wk1

## Types of Learning

+ Supervised Learning
  + Input & Output
+ Reinforcement Learning
  + Input & reward
+ Unsupervised Learning
  + Input Only

### Supervised Learning

+ Aim to **predict**

#### Issues

+ Frame work
+ representation
+ pre-processing
+ training method
  + perceptron, backpropagation
+ generalization
  + Ockham's razor
    + Avoid overfitting
+ evaluation

#### Two-Layer Neural Network

+ I-H-O
+ Error/Loss function
  + half of variance (analogy)

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
  + $w_0 = -threshold, x_0 = 1$
    + **Bias**
      + bias comes from +/- properties of threhold
      + Positive threshold->hard to fire
      + vice versa
+ **Transfer function**
  + $g(s)$
    + step function
    + sigmoid
    + hyperbolic tangent
+ $a=g(W\bar x+\bar b)$

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
      + or
      + $w- =\eta \frac{\partial E}{\partial w}$
        + *backpropagation
  + Effect: $s+=\eta(\sum(x_i^2))$
+ Vice versa

## Backpropagation

+ Supervised Learning
+ Multilayer
+ Adjusting $w$s using partial derivative
  + to get the derivative from a lower level, we need to calculate that of a higher level first, so it looks like reversing feedforward process of getting output.
+ method for calculating gradient then apply gradient descent.
