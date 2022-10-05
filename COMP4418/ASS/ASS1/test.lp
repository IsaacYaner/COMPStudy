% Determining the centre vertex
1{centre(X) : vertex(X)}1 :- .
% Generating leg/2
edge(Y,X) :- edge(X,Y).
1{leg(X,Y) : edge(X,Y)}2 :- vertex(X), not centre(X).
{leg(X,Y) : edge(X,Y)} :- vertex(X), centre(X).
leg(X,Y) :- leg(Y,X).
% Reachable
reachable(X) :- centre(X).
reachable(Y) :- reachable(X), leg(X,Y).
:- not reachable(X), vertex(X).
% Cycle
path(X,Y) :- leg(X,Y).
path(X,Z) :- path(X,Y), path(Y,Z), X!=Y, Y!=Z.
:- path(X,X).
#show centre/1.
#show leg/2.
% #show reachable/1.
#show.