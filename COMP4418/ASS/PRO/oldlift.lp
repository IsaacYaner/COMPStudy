#const capacity = 1.
person(1).
destination(1, 3).
pos(0, 1, 2).
ini(1, 2).

person(2).
destination(2, 5).
pos(0, 2, 4).
ini(2, 4).
% onlift(0, 1, a).
%pos(Time, object, floor)
%pos(Time, object, lift#)
lift(a).
destination(a, 5).
pos(0, a, 1).
direction(a, 1).
% lift(b).
% destination(b, 1).
% pos(0, b, 1).
% direction(b, 0).

% 只要有还没到终点的电梯，就没有停止
running(T) :- lift(L), pos(T, L, D), destination(L, D2), D!=D2.
% running(0).
running(T+1) :- not arrive(T, P), person(P), running(T), T<10.
pos(T+1, L, F+D) :- pos(T, L, F), direction(L, D), lift(L), running(T).

% T时刻，人的位置等于他所在的电梯的位置。
pos(T, P, F) :- person(P), onlift(T, P, L), pos(T, L, F), lift(L).
pos(T+1, P, F) :- pos(T, P, F), person(P), not onlift(T, P, L), lift(L), running(T). 
% T+1时刻，人仍然在电梯上
onlift(T+1, P, L) :- onlift(T, P, L), pos(T, P, F), not arrive(T, P).
% 人到想去的楼层
arrive(T+1, P) :- person(P), pos(T, P, F), destination(P, D), F=D, not arrive(T, P).
arrive(T+1, P) :- running(T), person(P), arrive(T, P).
% T时刻，人的层数等于电梯层数，并且人不在电梯上，就上电梯,      还要加上destination
onlift(T+1, P, L) :- not onlift(T, P, O), person(P), ini(P, F), pos(T, L, F), lift(L), lift(O), not arrive(T, P).

% 在T时刻，电梯上人的数量不大于capacity.
:- C = #count {P: onlift(T, P, L)}, lift(L), running(T), C > capacity.
% end(T) :- pos(T, L, D), lift(L), destination(L, D).

#show pos/3.
% #show onlift/3.
% #show arrive/2.
% #show running/1.

