%%% INPUT Initialization
% Initialise position of lifts
pos(0, L, F) :- liftini(L, F), lift(L), floor(F). 
% Initialize the waiting status of each user
waiting(0, Person, Floor) :- ini(Person, Floor), person(Person).
% Direction options and a placeholder for vip user and optimal upper bound
speed(1;-1). vip(0). 
#const upperlimit = maxtime.

%%% GENERATOR               
1{direction(T, L, D): speed(D)}1 :- lift(L), 0<=T<maxtime, canmove(T, L).
1 {assign(Person, L): lift(L)} 1 :- person(Person). 

%%% INFERENCE
%% Movement control strategy of the elevators
% the elevator can goingUp or goingDown iff 
% 1) users upstairs/downstairs are waiting for service or 
% 2) if no one is waiting then transport onlift user
canup(T, L) :- askingUp(T, L).
canup(T, L) :- not askingUp(T, L), onlift(T, L, P), pos(T, L, F), dest(P, Des), Des > F.
candown(T, L) :- askingDown(T, L).
candown(T, L) :- not askingDown(T, L), onlift(T, L, P), pos(T, L, F), dest(P, Des), Des < F.
                         
% If any direction is feasible then canmove is true                        
canmove(T, L) :- canup(T, L).
canmove(T, L) :- candown(T, L).
                                                  
% Transition of the elevators' position
pos(T+1, L, F+D) :- pos(T, L, F), direction(T, L, D), floor(F+D), time(T+1).    
    
%% Movement control strategy of the users    
% Keep waiting until the user walk in the elevator
waiting(T+1, Person, Floor) :- waiting(T, Person, Floor), assign(Person, L), not walkin(T, L, Person), time(T+1).
% Checking that whether has any user upstairs/downstairs are waiting                      
askingUp(T, L) :- waiting(T, P, F'),  pos(T, L, F), assign(P, L), F' > F.
askingDown(T, L) :- waiting(T, P, F'),  pos(T, L, F), assign(P, L), F' < F.                        

% Whether to enter the elevator is optional. This is made for dealing with the case 
% that more then one user enter the elevator at the same time with different directions                                           
{walkin(T, L, P)} 1:- assign(P, L), pos(T, L, F), waiting(T, P, F).
                         
% If the last frame a user is in the elevator, and the destination is not yet reached, stay in the elevator
onlift(T, L, P) :- walkin(T, L, P).                                                                    
onlift(T, L, P) :- onlift(T-1, L, P), pos(T, L, F), dest(P, Des), time(T), F != Des.
                          
% If user get to the floor he/she want to go to, marked as arrive
arrive(T, L, P) :- onlift(T-1, L, P), pos(T, L, F), dest(P, Des), time(T), Des=F.
arrive(P):- arrive(T, L, P).
arrive(P, T):- arrive(T, L, P).
                                                                  
%%% CONSTRAINS
% The elevator cannot move without permission to some directions
:- direction(T, L, 1), not canup(T, L).
:- direction(T, L, -1), not candown(T, L).

% Each user can not walkin elevator more than once
:- walkin(T, L, P), walkin(T', L, P),T != T'.
                         
% Users who get on the same elevator must in a same direction to their destination 
:- onlift(T, L, P1), onlift(T, L, P2), pos(T, L, F), dest(P1, D1), dest(P2, D2), D1 < F < D2.                         

% All the assignments must be finished
:- assign(Person, L), not arrive(Person).
                                                                        
% During the whole period, the load of each elevator should not exceed their capacity
load(T, Lift, Load) :- Load = #count {Person : onlift(T, Lift, Person)}, time(T), lift(Lift).
:- load(T, Lift, Load), Load>capacity.
                           
%%% OPTIMIZER                         
% optimizer for minimizing the latest arrival time 
% Recording the longest delivery time of all users
latestArrivalTime(T) :- T = #max {Time: arrive(P, Time), person(P)}. 
% Multi Optimizaion with priority                                              
#minimize {T@2:latestArrivalTime(T), time(T)}.
                          
%%% Extension 

% Recording the longest delivery time for vip user(s)
latersArrivalTimeVIP(T) :- T = #max {Time: arrive(P, Time), vip(P)}.
% Optimizer for VIP
#minimize {T@3:latersArrivalTimeVIP(T), time(T)}.                           

% filtering non-optimal-supermum model                   
:- arrive(P, Time), Time > upperlimit.
% optimizer for computing minimal total cost
totalArrivalTime(T) :- T = #sum {Time: person(P), arrive(P, Time)}, upperlimit < maxtime.
% will not using this optimizer with  default value of upperlimit only
totalArrivalTime(0) :- upperlimit >= maxtime. 
#minimize {T@1:totalArrivalTime(T)}.                           
                           
%%% OUTPUT 
#show pos/3.
#show assign/2.