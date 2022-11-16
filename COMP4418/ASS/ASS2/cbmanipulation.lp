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
winner(X) :- bordawinner(X).
winner(X) :- condorcetWinner(X).

1{cheater(I) : rank(I, X, C)}1 :- .
newrank(I, X, C) :- not cheater(I), rank(I, X, C).
1{newrank(I, X, C') : rank(I', X', C')}1 :- cheater(I), rank(I, X, C).
:- newrank(I, X, C), newrank(I, X', C), X!=X'.

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
:- cheater(I), newwinner(Xnew), winner(X), rank(I, X, R), rank(I, Xnew, Rnew), Rnew>=R.
fake(I, X, C) :- newrank(I, X, C), cheater(I).
original(I, X, C) :- rank(I, X, C), cheater(I).
% #show winner/1.
% #show cheater/1.
% #show newwinner/1.
#show fake/3.
#show original/3.
