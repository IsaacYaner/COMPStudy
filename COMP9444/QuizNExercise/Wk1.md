# Wk1

## Quiz 1

+ **What class of functions can be learned by a Perceptron?**

&emsp;Linear seperable function

+ **Explain the difference between Perceptron Learning and Backpropagation.**

&emsp;Perceptron learning only involves one perceptron. Backpropagation is a process to calculate partial derivative in the learning process of a multy-layer neural network.

+ **When training a Neural Network by Backpropagation, what happens if the Learning Rate is too low? What happens if it is too high?**

&emsp;If the rate is too low ???
&emsp;If the rate is too high, the weights may pass over the desired value.

+ **Explain why rescaling of inputs is sometimes necessary for Neural Networks.**

&emsp;Because different input has different range, sometimes a too big or too small value may have negative impact on accuracy.

+ **What is the difference between Online Learning, Batch Learning, Mini-Batch Learning and Experience Replay? Which of these methods are referred to as "Stochastic Gradient Descent"?**

+ ??? What is Online Learning
+ ??? What is Batch learning 
+ Mini batch is a process of deviding the training set to some small subset to speed up the learning process.
+ ??? What is Experience replay
+ Stochastic gradient Decsent is Mini-Batch

## Exercise 1

+ **Q1**

$w_0$|$w_1$|$w_2$
-|-|-
-1|0.4|0.9
$-w_0<w_1+w_2<-\frac{3}{2}w_0$
$w_2<-w_0$
$w_1<-\frac{1}{2}w_0$

+ **Q2**

Iteration|$w_0$|$w_1$|$w_2$|Training Example|$x_1$|$x_2$|Class|s|Action
-|-|-|-|-|-|-|-|-|-
1|-1.5|0|2|a|0|1|-|+0.5|Subtract
2|-2.5|0|1|b|2|0|-|-2.5|None
3|-2.5|0|1|c|1|1|+|-1.5|Add
4|-1.5|1|2|a|0|1|-|+0.5|Subtract
5|-2.5|1|1|b|2|0|-|-0.5|None
6|-2.5|1|1|c|1|1|-|-0.5|Add
7|-1.5|2|2|a|0|1|-|+0.5|Subtract
8|-2.5|2|1|b|2|0|-|+1.5|Subtract
9|-3.5|0|1|c|1|1|-|-2.5|Add
10|-2.5|1|2|a|0|1|-|-0.5|Subtract

## Exercise 2

1
0.5?

2 
$O=c(c(I^TW^{HI}-\bold b^H)^TW^{OH}-\bold b^O)$
Can be re-written in $ccI^T + constant$ form.
