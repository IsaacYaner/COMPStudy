const = 5.
vertex(a). % centre
vertex(b).
vertex(c).
vertex(d).
vertex(e).

edge(a,b).
edge(a,c).
edge(b,d).

path(X,Y) :- edge(X,Y).
path(X,Z) :- path(X,Y), path(Y,Z).
influence(X, D) :- vertex(X), D = #count {I: path(X, I)}.

% #show path/2.
#show influence/2.
