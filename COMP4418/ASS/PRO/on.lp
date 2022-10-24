person(p).
on(1, p, 1).
on(T+1, P, L) :- on(T, P, L), T=1.