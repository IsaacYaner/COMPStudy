a(1).
b(2).
c(X):-a(X).
c(X):-b(X).
f(X):-c(X), not b(X).

