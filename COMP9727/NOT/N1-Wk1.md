# Wk1

## Userbased collaborate rating

### Similarity 

+ Jaccard 
  + $\frac{U_i \bigcap U_j}{U_i \bigcup U_j}$
+ Cosine 
  + $\frac{\Sigma U_iU_j}{\sqrt{\Sigma U^2}\sqrt{\Sigma U^2}}$
  + Works well for sparse dataset
+ Pearson correlation
  + $\frac{\Sigma(r-\overline r)(r-\overline{r})}{\sqrt{\Sigma(r-\overline r)^2}\sqrt{\Sigma(r-\overline r)^2}}$

### Predict

+ mean + weighted average of (similar(i,j))*(markj-meanj)

### Pick neighbours

+ Positive only
+ 50-200 ok
+ Can divide by sqrt(P/k)

### Improvement

+ recount Valuable

## Item based

+ Flip
+ More static

## Cold start

## Rating 

+ Test with real users
  + AB test
+ Lab tests
  + Controlled experiments
+ Offline experiments
  + fitting
+ Simulator

### Features

+ Diversity
+ Coverage
+ Serendipity


### Accuracy

+ Precision:
  + exactness: relevant/all got
  + tp/tp+fp
  + tp/tp+fn
+ Recall:
  + completeness: relevant/all potential

#### DCG

+ nDCG = DCG/ideal matches

## CF

### Matrix

+ Singular value decomposition
+ Matrix Factorisation

#### SVD

+ Dimensionality Reduction
+ Workflow
  + Given A, find U,Vt,Sigma
+ Usage
  + U = user*category
  + Sigma = weight of category
  + Vt = category*movie
+ Can't handle missing values

#### Matrix Factorisation

+ min Σ (r-qp)^2 + λ(q^2 + p^2)
+ Learning
  + Stochastic gradient descent
    + SGD
  + Alternating least squares
    + ALS
    + Fix one, adjust another, switch, repeat until converge

### Locality Sensitive Hashing

+ 
