%% this problem simulates the Commuting time
%% all persons on different floors want to go to the ground floor
%% A simulation of after-work rush hour
%% this file also tests our vip extensions

#const maxtime = 47. 
#const capacity = 8. 
time(0..maxtime). 
floor(1..10). 

lift(l1). liftini(l1, 1). 
lift(l2). liftini(l2, 1). 
lift(l3). liftini(l3, 1). 

person(issac). ini(issac, 2). dest(issac, 1). 
person(isla). ini(isla, 5). dest(isla, 1). 
person(kepling). ini(kepling, 4). dest(kepling, 1). 
person(austin). ini(austin, 4). dest(austin, 1). 
person(alan). ini(alan, 10). dest(alan, 1). 
person(albert). ini(albert, 4). dest(albert, 1). 
person(ben). ini(ben, 3). dest(ben, 1). 
person(bill). ini(bill, 3). dest(bill, 1). 
person(brad). ini(brad, 9). dest(brad, 1). 
person(brent). ini(brent, 10). dest(brent, 1). 
person(brown). ini(brown, 9). dest(brown, 1). 
person(bert). ini(bert, 9). dest(bert, 1). 
person(carl). ini(carl, 7). dest(carl, 1). 
person(cary). ini(cary, 5). dest(cary, 1). 
person(chris). ini(chris, 7). dest(chris, 1). 
person(cole). ini(cole, 2). dest(cole, 1). 
person(colin). ini(colin, 3). dest(colin, 1). 
person(cosmo). ini(cosmo, 7). dest(cosmo, 1). 
person(daniel). ini(daniel, 7). dest(daniel, 1). 
person(denny). ini(denny, 7). dest(denny, 1). 
person(david). ini(david, 2). dest(david, 1). 
person(dennis). ini(dennis, 5). dest(dennis, 1). 
person(dylan). ini(dylan, 8). dest(dylan, 1). 
person(eddie). ini(eddie, 7). dest(eddie, 1). 
person(edgar). ini(edgar, 7). dest(edgar, 1). 
person(edwin). ini(edwin, 5). dest(edwin, 1). 
person(elliott). ini(elliott, 10). dest(elliott, 1). 
person(eric). ini(eric, 7). dest(eric, 1). 
person(elvis). ini(elvis, 4). dest(elvis, 1). 
person(frank). ini(frank, 4). dest(frank, 1). 
person(ford). ini(ford, 5). dest(ford, 1). 
person(fred). ini(fred, 9). dest(fred, 1). 
person(gino). ini(gino, 4). dest(gino, 1). 
person(gavin). ini(gavin, 2). dest(gavin, 1). 
person(george). ini(george, 3). dest(george, 1). 
person(hank). ini(hank, 2). dest(hank, 1). 
person(henry). ini(henry, 5). dest(henry, 1). 

%% extension
vip(kepling). vip(issac). vip(isla).