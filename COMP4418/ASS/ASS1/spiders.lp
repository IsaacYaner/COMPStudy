% Determining the centre vertex
1{centre(X) : vertex(X)}1 :- .

% Generating leg/2
% Make edge undirected.
edge(Y,X) :- edge(X,Y).
% At most one outdegree.
 {leg(X,Y) : edge(X,Y)}1 :- vertex(X), not centre(X).
% Exactly one indegree
1{leg(Y,X) : edge(X,Y)}1 :- vertex(X), not centre(X).
% No limit on out degree for centre
% No indegree.
 {leg(X,Y) : edge(X,Y)}  :- vertex(X), centre(X).

% Cycle
path(X,Y) :- leg(X,Y).
path(X,Z) :- path(X,Y), path(Y,Z).
:- path(X,X).
% Reachable from centre
:- not path(X,Y), centre(X), vertex(Y), X!=Y.

#show.
#show centre/1.
#show leg/2.
% #show reachable/1.