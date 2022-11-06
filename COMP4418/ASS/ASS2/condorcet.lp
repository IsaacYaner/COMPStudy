% count number of times candidate X wins head-to-head against Y.
win(X, Y, C) :- C = #count {I: rank(I, X, C1), rank(I, Y, C2), C1<C2}, rank(IX, X, CX), rank(IY, Y, CY), X!=Y.
% Y is dominated when win fewer times than X.
dominated(Y) :- win(X, Y, C1), win(Y, X, C2), C1 > C2.
% condercet winner is the one who never been dominated
condorcetWinner(W) :- not dominated(W), rank(V, W, K).

#show condorcetWinner/1.