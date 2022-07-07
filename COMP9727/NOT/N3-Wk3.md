# Week 3

## FM

+ Feature Machine

|user|f1|f2|
|-|-|-|
|u1|score|score|

## Association Rules

+ Item set
+ Support count
  + occurence of item set
+ Support
  + occurence rate
+ Frequent Itemset
  + count ge threshold
+ Associative rule
  + $A\rightarrow B(s, c)$
  + The possibility of(all elements) this rule and effectiveness of this rule
  + implication
  + Support
    + See above
  + Confidence
    + How often Y occurs given X
+ Rule evaluation matrics

### Goal

+ Find all rules having
  + support ge minsup threshold
  + confidence ge minconf

### Prune

+ Apriori
  + If subset not frequent, it will also be infrequent

### Rule generation

+ Merging two other rules
+ $A_1\rightarrow B_1$
+ $A_2\rightarrow B_2$
+ $A_1\cap A_2\rightarrow B_1\cup B_2$
+ Validate by confidence

+ Can be used to generate classification result
+ Laplace prior

## Learn to rank

+ Pointwise
  + $f(user, item)$
+ Pairwise
  + $f(user, item_1, item_2)$
+ Listwise
  + $f(user, [item_i])$

## Eigen Rank

+ Accuracy in prediction may not represent higher ranking effectiveness
+ Kendall Rank
  + Similarity in ranking
  + Relax assumption on transitivity

### Methods

+ Greedy Order
+ Random Walk

## BPR

+ Implicit Feedback
  + Purchase\click -- only positive data
+ 

## Question

+ BPR
