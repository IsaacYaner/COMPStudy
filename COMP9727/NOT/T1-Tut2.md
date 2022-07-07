# Tut2

## SVD

+ Calculate $AA^T$ and $A^TA$
+ For left one
    + Get eigenvalue by $det(AA^T-\lambda I)$
    + Get eighen vectors 
    + Concat the vectors to get $U$
+ For right one
  + Get eigenvalue by $det(A^TA-\lambda I)$
  + Get stretching matrix of singular values $\Sigma=diagonal\ \sqrt{\lambda}$
  + Get eighen matrix $V$

## Collaborative filtering

+ PCC distance
+ cal $\bar r_u$ for each user
+ 
