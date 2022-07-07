# Week 2

## Improvement to CF

+ Divide by $\sqrt{P_u(i)/k}$ to normalise
+ bias
  + $b_{ui} = \mu_u + b_u + b_i$
+ weighted average rate bias deviation of {k} similar items
  + warb
+ $\hat{r}_{ui}=b_{ui}+warb/norm+\Sigma sim(R^k(i), u's\ experience)/norm$
  + Latent Factor model

### Problems

+ scaling issue
+ idle user

## PMF

+ log MSE
+ Converge to SVD if all ratings are observed
+ Complexity control
  + auto choosing priors
+ Limitation
  + Few ratings - close to prior mean/average user

### Constrained PMF

+ Introduce W and I
+ Many other balabala variations of PMF

### Bayesian PMF

+ W: Wishart distribution

## Question

+ What is ALS
+ What is CF
  + Collaborative Filter
+ What is MF
+ What is SVD
  + U $\Sigma$ V
+ What is Frobenius norm
