% count number of times candidate X wins head-to-head against Y.
win(X, Y, C) :- C = #count {I: rank(I, X, C1), rank(I, Y, C2), C1<C2}, rank(IX, X, CX), rank(IY, Y, CY), X!=Y.
% Y is dominated when win fewer times than X.
dominated(Y) :- win(X, Y, C1), win(Y, X, C2), C1 >= C2.
% condercet winner is the one who never been dominated
condorcetWinner(W) :- not dominated(W), rank(V, W, K).

calborda(0) :- condorcetWinner(X).
calborda(1) :- not calborda(0).

% Calculate score for each rank
score(I, X, N-C) :- rank(I, X, C), N = #count {X' : rank(I, X', C)}.
% Calculate total score for each candidate
total(X, T) :- T = #sum {S : score(I, X, S)}, score(IX, X, SX).
% Get highest score
highest(S) :- S = #max {Score : total(X, Score)}.
% List the candidate with highest score
satisfied(X) :- total(X, H), highest(H).
% Set the name with first alphabetical order winner
bordawinner(X) :- calborda(1), X = #min {Name : satisfied(Name)}.
#show bordawinner/1.
#show condorcetWinner/1.