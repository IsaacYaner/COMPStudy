# Neural Network

+ Neurons
+ Perceptron
+ Linear separability
+ Multi-Layer Networks
+ Backpropagation
+ Applications

## Neurons

### McCulloch &  Pitts

+ of a single neuron

#### Activation functions

+ receive weighted sum and output.

## Perceptron

+ Single layere feed forward neural network
+ Can only compute a linear separable function
+ Use sigmoid as activation
  + sigmoid
    + $\frac{1}{1+e^{-s}}$
    + derivative = $z(1-z)$
  + tanh
    + derivative = $1-z^2$

### Linear Separability

+ bias is propotional to offset from origin
+ weights determine slope
+ weight vector is perpendicular to the plane
+ Use multi-layer to learn non separable
  + kernel trick?

### Perceptron Learning algorithm

+ adjust weight by comparing
+ Training set: set of input vectors
+ $\eta$ as learning rate
  + small steps lessen possibility of destroying correct classifications
+ Initial some $w_i$
+ $w_i = w_i+\eta(d-y)\times x_i$
  + d : desired
  + y : actual

#### Perceptron Convergence Theorem

+ For any separable set, the learning rule guaranteed to find solution in finite iterations

#### Feed forward network

+ parameterized family of nonlinear functions
+ Calculation: from input to output
+ Learning: Back propagate

##### Error

$E=\frac{1}{2}\Sigma(z-t)^2$
$w=w-\eta\frac{dE}{dw}$

## Applications

## Structure

+ Feed forward
  + one direction
+ Recurrent
  + feed output back
+ They have
  + input
  + hidden
  + output
