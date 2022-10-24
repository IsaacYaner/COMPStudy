#const maxtime = 100.
% 按键
% 现在是这样的，每层都会在某一时刻被按键，电梯会在没有
% 按键的时候停止，目标是最小化停止的时间。
% 电梯到特定层数的时候，那层的按键就会灭掉。
% 后续可以加上人会取按按钮。
floor(1..10).
up(0, 3).

lift(a).
pos(0, a, 2).
% lift(b).
% pos(0, b, 4).

% 按键亮的指令
pressed(T, F) :- up(T, F).
pressed(T, F) :- down(T, F).
% 电梯到这个楼层就会关掉按钮
turnoff(T, F) :- pos(T, L, F).
up(T+1, F) :- up(T, F), not turnoff(T, F), T<maxtime.
down(T+1, F) :- down(T, F), not turnoff(T, F), T<maxtime.
% 电梯只能有一个方向，如果能上下则不停。
canup(T, L) :- pressed(T, F'),  pos(T, L, F), F'>F.
candown(T, L) :- pressed(T, F'),  pos(T, L, F), F'<F.
:- direction(T, L, -1), not candown(T, L).
:- direction(T, L, 1), not canup(T, L).
:- direction(T, L, 0), canup(T, L).
:- direction(T, L, 0), candown(T, L).
1{direction(T, L, D): -1<=D<=1}1 :- lift(L), 0<=T<maxtime, pressed(T, F), floor(F).
% 电梯移动 后续可以加上是否在上人过程中
pos(T+1, L, F+D) :- pos(T, L, F), direction(T, L, D).
#minimize {T:pressed(T, F), T>0}.
% #show direction/3.
% #show pressed/2.
#show pos/3.
% #show up/2.
% #show canup/2.
