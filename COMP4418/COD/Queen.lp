#const n=4.
queen(1..n).

1{place(X, Y) : 0<Y<n+1}1 :- queen(X).
:- place(I, Y), place(J, Y), I!=J.
:- place(X, Y), place(X', Y'), X!=X', X-Y==X'-Y'.
:- place(X, Y), place(X', Y'), X!=X', X+Y==X'+Y'.

% #show .
% #show place/2.