#const load=4.
#const nump=3.
#const numl=3.
lift(a).
lift(b).
person(1).
person(2).
person(3).
destination(1, 3).
destination(2, 4).
destination(3, 1).
%pos(Time, object, floor)
pos(0, 1, 1).
pos(0, 2, 2).
pos(0, 3, 3).
pos(0, a, 1).
pos(0, b, 2).
% status(lift, direction, capacity) direction={-1,0,1}
status(a, 0, 0).
status(b, 0, 0).

% 状态转移
pos(T+1, L, F+D) :- pos(T, L, F), status(L, D, C), lift(L), operating(T), not loading().
% 人到了就不动了
arrive(P, T) :- pos(T, P, D), destination(P, D), person(P).
% 结束
dist(X, D) :- vertex(X), D = #count {I: path(I, X)}
operating(T+1) :- N = #count {P: arrive(P)}, N < nump, finish(T).
finish(T) :- N = #count {T,L,F : pos(T,L,F)}, N=numl.
%方向相同 并且没有超重
% 电梯加重，人改变状态 :- .
% 当方向是0并且人在其它楼层，T+1时刻改变方向。
end(T) :- N = #count{P: arrive(P, T)}, N=nump.
minimize end(T).
% 不能超重
:- status(L, D, C), C>4.