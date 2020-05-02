# Unsupervised learning and Decision tree

+ Learning Agent
+ Inductive learning
+ Decision tree leaning

## Learning Agent

+ Aim to improve performance on future tasks after making observations about the world
+ Focus on classifying things

## Supervised Learning 

+ Training set and Test set
  + Set of items
  + each item has attributes and a class or target value
+ Decision Tree
+ Neural Network
+ Support Vector Machine
+ Can not use test set to learn

### Methodology

+ Select feature
+ Choose representation
+ Pre-process
+ Choose learning method
+ Choose training regime
+ Evaluation

## Inductive learning

+ given $x, f(x)$ pairs, find h.
  + h is consistent if agrees with f in all examples

### Ockham's Razor (Occam)

+ Choose simplest consistent

## Decision Tree Learning

+ Not binary tree
+ Approximating discrete functions
+ Widely used for inductive inference

### ID3

+ Discrete
+ Greedy
+ Partition according to Features
+ Must be consistent training data
+ Good attribute splits examples to all T or all F
  + Then the tree can be smaller
  + Use information to selectr attribute 
    + Information = - probability
  + Entropy = $H(<p_1,...,p_n>)=-\Sigma p_ilog_2p_i$
    + Then entropy is the bits required to encrypt

#### Entropy

+ Measure of randomness
+ Information reduces entropy
+ Measure information in bits

&emsp;For a decision tree, $H(<\frac{p}{p+n},\frac{n}{p+n}>)$ is the entropy of one branch
&emsp;For all branches, namely current node
$\Sigma \frac{p_i+n_i}{p+n}H(<\frac{p_i}{p_i+n_i},\frac{n_i}{p_i+n_i}>)$

### Performance measurement

+ Methods
  + Use computation/statistical theory
  + Test
    + use same distribution over examplesapce as training set
+ Learning curve
  + % correct, x is training set size

### Pruning

+ Prun noisy data
+ Methods
  + Use pruning set, i.e. try
  + Use data to estimate error
+ Only prune if error is less
+ Laplace error
  + $E=1-\frac{n+1}{N+k}$
    + n = number of majority class
    + N = total number
    + k = number of classes
  + If average E exceed that of parent node, prune
    + The average is weight average by the probability

## Other TDIDT algorithms

+ ID3
+ CART
+ Assistant
+ C4.5
+ C5
+ Treesin WEKA
+ scikit-learn

## Regression trees

+ Continuous
+ algs
  + CART
  + RETIS
  + M5
  + WEKA

## Training and Testing

+ Measure error rate

### Ways

+ Self-consistency
  + Use training set to test
+ Hold out strategy
  + Use some data to test, use some to train
  + Need large database
+ K-fold Cross validation technique
  + Seperate in to k equal sets, take one to test, another to train, do k times
    + Leave-One-Out
    + We can leave more out
  + Final accuracy is mean value of k trials
