dist(X, D) :- vertex(X), D = #count {I: path(I, X)}.
longest(M) :- M = #max {D:dist(X,D), vertex(X)}.
#minimize {M:longest(M), M>0}.
#show longest/1.
#show dist/2.