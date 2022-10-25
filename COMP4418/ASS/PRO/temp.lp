

#const floorNum=3.
#const maxTime=20.


lAction(move;stop;).

% envir setup
% person(PID, StartingFloor, Destination)
person(alice, 2, 3).
person(bob, 3, 1).

% lift(LiftID)
lift(lift_1).

% const
speed(1;0;-1).
time(0..maxTime).
floor(1..floorNum).


% initial status for person and lift
% for lift: liftStatus(LiftID, Floor, Speed, LiftAction, T).
liftStatus(LiftID, 1, 0, stop, 0) :- lift(LiftID).

% for person: personStatus(PID, Floor, Destination, Dir, checkPoint).
personStatus(PID, Start, Des, 1, start):- person(PID, Start, Des), Des > Start.
personStatus(PID, Start, Des, -1, start):- person(PID, Start, Des), Des < Start. 
person(PID):- person(PID, Start, Des).

% generator
{liftStatus(LiftID, Floor, Speed, LiftAction, T):lift(LiftID), floor(Floor), speed(Speed), lAction(LiftAction), time(T)}.
{onLift(PID, LiftID, T): person(PID), lift(LiftID),time(T)}.

% cost
cost(PID, Val):- person(PID), Val = #count {T:onLift(PID,_,T)}. 
total_cost(Val1):- Val1 =#sum {Cost:cost(_, Cost)}.
userNum(Val):- Val = #count {PID:person(PID)}.
:- cost(PID, Val), Val<1.

% one lift for one person
:- onLift(PID, L1, _), onLift(PID, L2, _), L1 != L2.
% 上电梯时电梯必须停在这一层
:- onLift(PID, LiftID, T), personStatus(PID, Start, _, _, start), not onLift(PID, LiftID, T-1), liftStatus(LiftID, L, _, _, T), L!=Start.
:- onLift(PID, LiftID, T), personStatus(PID, Start, _, _, start), not onLift(PID, LiftID, T-1), liftStatus(LiftID, _, _, move, T).
% 在电梯里必须和其他人同方向
:- onLift(P1, LiftID, T), onLift(P2, LiftID, T), personStatus(P1, _, _, Dir1,start),personStatus(P2, _, _, Dir2,start), Dir1 != Dir2.
% 到过终点必须下电梯, 不再续约onlift关系.
:- onLift(PID, LiftID, T),  onLift(PID, LiftID, T+1), personStatus(PID, _, Des, _, start), liftStatus(LiftID, Des, _, _, T).
% 终点
personStatus(PID, Start, Des, Dir, end):- onLift(PID, LiftID, T),  not onLift(PID, LiftID, T+1), personStatus(PID, Start, Des, Dir, start).
:- personStatus(PID, Start, Des, Dir, end), T1 = #max{T:onLift(PID, LiftID, T)},  onLift(PID, LiftID, _), liftStatus(LiftID, _, _, move, T1).
:- personStatus(PID, Start, Des, Dir, end), T1 = #max{T:onLift(PID, LiftID, T)},  onLift(PID, LiftID, _), liftStatus(LiftID, F, _, _, T1), F!=Des.

% 必须收敛
:- personStatus(PID, Start, Des, Dir, start), not personStatus(PID, Start, Des, Dir, end).

% only one action\speed\floor at a time for each lift
:- liftStatus(LiftID, _, _, Action_1, T), liftStatus(LiftID, _, _, Action_2, T), Action_1 != Action_2.
:- liftStatus(LiftID, _, S1, _, T), liftStatus(LiftID, _, S2, _, T), S1 != S2.
:- liftStatus(LiftID, F1, _, _, T), liftStatus(LiftID, F2, _, _, T), F1 != F2.
    
% record status for the whole period 
T = maxTime :- liftStatus(LiftID, _, _, _, T), not liftStatus(LiftID, _, _, _, T+1).

% checking whether is a vaild action series

% rules for speed limit
:- liftStatus(_, 1, S, _, _), S<0.
:- liftStatus(_, floorNum, S, _, _), S>0.
% rules for move
:- liftStatus(_, _, S, move, _), S=0.
:- liftStatus(LiftID, F1, S, move, T), liftStatus(LiftID, F2, _, _, T+1), F2 != F1 + S.
% 电梯移动的方向必须和当前onLift的所有人目标方向相同
:- liftStatus(LiftID, _, S, move, T), onLift(PID, LiftID, T),  personStatus(PID, _, _, Dir, start), Dir!=S.
% 如果当前onLift的人有要下的, 必须停止
:- liftStatus(LiftID, Des, _, move, T), onLift(PID, LiftID, T), personStatus(PID, _, Des, _, start), not personStatus(PID, _, Des, _, end).
% rules for stop
:- liftStatus(_, _, S, stop, _), S!=0.
:- liftStatus(LiftID, F1, 0, stop, T), liftStatus(LiftID, F2, _, _, T+1), F1 != F2.



#minimize {Val:total_cost(Val)}.
#show liftStatus/5.
#show onLift/3.
#show total_cost/1.


