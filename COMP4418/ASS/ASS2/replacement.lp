% count number of times candidate X wins head-to-head against Y.
newwin(X, Y, C) :- C = #count {I: newrank(I, X, C1), newrank(I, Y, C2), C1<C2}, newrank(IX, X, CX), newrank(IY, Y, CY), X!=Y.
% Y is dominated when win fewer times than X.
newdominated(Y) :- newwin(X, Y, C1), newwin(Y, X, C2), C1 >= C2.
% condercet winner is the one who never been dominated
newcondorcetWinner(W) :- not newdominated(W), newrank(V, W, K).

newcalborda(0) :- newcondorcetWinner(X).
newcalborda(1) :- not newcalborda(0).

% Calculate score for each rank
newscore(I, X, N-C) :- newrank(I, X, C), N = #count {X' : newrank(I, X', C)}.
% Calculate total score for each candidate
newtotal(X, T) :- T = #sum {S : newscore(I, X, S)}, newscore(IX, X, SX).
% Get highest score
newhighest(S) :- S = #max {Score : newtotal(X, Score)}.
% List the candidate with highest score
newsatisfied(X) :- newtotal(X, H), newhighest(H).
% Set the name with first alphabetical order winner
newbordawinner(X) :- newcalborda(1), X = #min {Name : newsatisfied(Name)}.
newwinner(X) :- newbordawinner(X).
newwinner(X) :- newcondorcetWinner(X).