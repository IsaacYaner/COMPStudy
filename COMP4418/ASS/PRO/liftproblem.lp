% 数据部分
#const maxtime = 20.
#const capacity = 1.
floor(1..10).
time(0..maxtime).

% 电梯的初始状态只有pos
lift(a).
pos(0, a, 2).
lift(b).
pos(0, b, 2).

% 人的初始状态只有ini和dest
person(alice).
ini(alice, 7).
dest(alice, 4).

person(bob).
ini(bob, 7).
dest(bob, 4).

% 电梯和灯光部分的代码

% 现在是这样的，每层会在某一时刻被按键，电梯会在没有
% 按键的时候并且电梯上没人的时候停止，目标是最小化停止的时间。
% 按键亮的指令
% 电梯到这个楼层就会关掉按钮
turnoff(T, F) :- pos(T, L, F).
pressed(T+1, F) :- pressed(T, F), not turnoff(T, F), T<maxtime.
% down(T+1, F) :- down(T, F), not turnoff(T, F), T<maxtime.
% 电梯只能有一个方向，如果能上下则不停。
canup(T, L) :- pressed(T, F'),  pos(T, L, F), F'>F.
canup(T, L) :- goto(T, L, F'), pos(T, L, F), F'>F.
candown(T, L) :- pressed(T, F'),  pos(T, L, F), F'<F.
candown(T, L) :- goto(T, L, F'),  pos(T, L, F), F'<F.
canmove(T, L) :- pressed(T, F), lift(L).
canmove(T, L) :- goto(T, L, F), lift(L).
:- direction(T, L, -1), not candown(T, L).
:- direction(T, L, 1), not canup(T, L).
:- direction(T, L, 0), canup(T, L).
:- direction(T, L, 0), candown(T, L).
1{direction(T, L, D): -1<=D<=1}1 :- lift(L), 0<=T<maxtime, canmove(T, L), floor(F).
% 电梯移动
pos(T+1, L, F+D) :- pos(T, L, F), direction(T, L, D).




% 下面是人上下电梯部分的代码
% 初始化人物的等待状态
waiting(0, Person, Floor) :- ini(Person, Floor), person(Person).

% 以下分别是
% 等电梯的逻辑             上电梯的逻辑    
% 上电梯之后按楼层的逻辑    和下电梯的逻辑

% 人在等电梯的时候就要按键，如果人不在电梯上就一直等
pressed(T, Floor) :- ini(Person, Floor), waiting(T, Person, Floor), person(Person), time(T).
waiting(T+1, Person, Floor) :- waiting(T, Person, Floor), not onlift(T, Person), time(T).
onlift(T, Person) :- pick(T, Lift, Person), person(Person), time(T), lift(Lift).

% 人只有在电梯到达的时候才会在下一刻上电梯
% 第0时刻不会上电梯
:- onlift(0, Person), person(Person).
:- onlift(T+1, Person), not onlift(T, Person), pos(T+1, Lift, Floor), ini(Person, FW), Floor!=FW , person(Person) , lift(Lift), time(T).

% 每个人同时被最多一个电梯pick
{pick(T, Lift, Person) : lift(Lift)}1 :- person(Person), time(T).

% 人被pick以后就再也不可能waiting了
pick(T+1, Lift, Person) :- pick(T, Lift, Person), not arrive(T, Person), person(Person), time(T), pick(Lift).
:- pick(T, Lift, Person), waiting(T', Person, Floor), T'>T, person(Person), time(T), floor(Floor), lift(Lift).

% goto代表电梯要去几层，也就是按了按钮
goto(T, Lift, Floor) :- pick(T, Lift, Person), waiting(T, Person, FloorW), turnoff(T, FloorW), dest(Person, Floor), time(T), lift(Lift).
goto(T+1, Lift, Floor) :- goto(T, Lift, Floor), not turnoff(T, Floor), time(T), lift(Lift).

% 如果到了想去的楼层,就下电梯，标记arrive。
% 人在到达之后永远都是arrive的状态了。
arrive(T+1, Person) :- arrive(T, Person), person(Person), time(T).
arrive(T, Person) :- pick(T, Lift, Person), pos(T, Lift, Floor), dest(Person, Floor), person(Person), time(T).



% 结束的部分
% 只要电梯里面的灯都灭了,并且没有人在等待了就都算结束。
1{end(T):time(T)}.
:- end(T), waiting(T, Person, Floor), person(Person), floor(Floor).
:- end(T), goto(T, Lift, Floor), lift(Lift), floor(Floor).
% 必须所有人都arrive才行
numperson(N) :- N = #count{Person : person(Person)}.
:- Numarr = #count{Person : arrive(T, Person), earlist(T)}, Numarr != N, numperson(N).


% 限制电梯的人数
load(T, Lift, Load) :- Load = #count {Person : pick(T, Lift, Person)}, time(T), lift(Lift).
:- load(T, Lift, Load), lift(Lift), Load>capacity, time(T).


% 最后优化部分
earlist(Early) :- Early = #min {T : end(T)}.
#minimize {E:earlist(E)}.

% 显示运行轨迹
#show pos/3.

% #show direction/3.
% #show pressed/2.
% #show pos/3.
% #show up/2.
% #show canup/2.
% #show waiting/3.
% #show end/1.
% #show goto/3.
% #show pick/3.
% #show waiting/3.
% #show onlift/2.
% #show load/3.
% #show arrive/2.
% #show earlist/1.
