# Wk2

## Probability

### Bayes' Rule

+ P(A N B) = P(A|B)P(B)

### entropy

+ $H(p) = \Sigma ^n_{i=1}p_i(-log_2p_i)$
  + For continuous, replace sum by integral
  + For multivariate Normal,
    + $H = \Sigma_ilog\sigma_i$

### KL Divergence

+ Kullback-Leibler Divergence
+ $D_{KL}(p||q)=\Sigma^n_{i=1}p_i(log_2p_i-log_2q_i)$
  + Not Symmetric
    + Based on p, if we get q
    + If we invert, the be based on q, if we get p
    + So it's not symmetric

#### Forward KL (P||Q)

+ P is actual, Q is sample
+ must straddle to cover each

#### Reverse KL (Q||P)

+ cover either
+ WHY?
  + mechanism?

## Variations on Backpropgation

+ Cross Entropy
+ Weight Decay
+ Momentum

### Cross Entropy

+ $E=-tlog(z)-(1-t)log(1-z)$
+ denominator of derivative is derivative of sigmoid.

#### Likelihood

+ $logP(D|h)$ is likelihood

