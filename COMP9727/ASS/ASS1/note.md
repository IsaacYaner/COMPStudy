# ASS

## Question 1

+ Confidence
  + $conf(X \rightarrow Y)$
  + That is,
  + $P(Y|X)$
+ Lift
  + $lift(X \rightarrow Y) = \frac{conf(X \rightarrow Y)}{support(Y)}$
+ Conviction
  + $conv(X \rightarrow Y) = \frac{1-support(Y)}{1-conf(X \rightarrow Y)}$
  + $Support(Y)$ can be view as $conf(X \rightarrow Y)$ given $X$ and $Y$ are independent.
  + $\frac{independent\ incorrect}{real\ incorrect}$
  + If convic > 1:
    + if they are independent, the incorrect rate would be higher.
