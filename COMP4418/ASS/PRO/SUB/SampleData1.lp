%% this is just a random situation
%% this data file is used to test the MVP, without any extension
%% if you want to test with smallest total time extension, you should add '-c upperlimit=...' before running
%% NOTE: The smallest total time optimization with upperlimit paramater could be time comsuming



#const maxtime = 43. 
#const capacity = 8. 
time(0..maxtime). 
floor(1..10). 

lift(l1). liftini(l1, 10). 
lift(l2). liftini(l2, 6). 
lift(l3). liftini(l3, 4). 

person(issac). ini(issac, 9). dest(issac, 1). 
person(isla). ini(isla, 8). dest(isla, 3). 
person(kepling). ini(kepling, 8). dest(kepling, 10). 
person(austin). ini(austin, 6). dest(austin, 10). 
person(alan). ini(alan, 2). dest(alan, 10). 
person(albert). ini(albert, 2). dest(albert, 10). 
person(ben). ini(ben, 10). dest(ben, 6). 
person(bill). ini(bill, 3). dest(bill, 9). 
person(brad). ini(brad, 3). dest(brad, 8). 
person(brent). ini(brent, 5). dest(brent, 4). 
person(brown). ini(brown, 9). dest(brown, 10). 
person(bert). ini(bert, 7). dest(bert, 8). 
person(carl). ini(carl, 5). dest(carl, 7). 
person(cary). ini(cary, 7). dest(cary, 10). 
person(chris). ini(chris, 8). dest(chris, 4). 
person(cole). ini(cole, 2). dest(cole, 3). 
person(colin). ini(colin, 4). dest(colin, 1). 
person(cosmo). ini(cosmo, 3). dest(cosmo, 2). 
person(daniel). ini(daniel, 9). dest(daniel, 10). 
person(denny). ini(denny, 4). dest(denny, 2). 
person(david). ini(david, 5). dest(david, 4). 
person(dennis). ini(dennis, 7). dest(dennis, 3). 
person(dylan). ini(dylan, 2). dest(dylan, 4). 
person(eddie). ini(eddie, 4). dest(eddie, 1). 
person(edgar). ini(edgar, 10). dest(edgar, 2). 
person(edwin). ini(edwin, 3). dest(edwin, 2). 
person(elliott). ini(elliott, 5). dest(elliott, 4). 
person(eric). ini(eric, 8). dest(eric, 4). 
person(elvis). ini(elvis, 4). dest(elvis, 5). 
person(frank). ini(frank, 9). dest(frank, 8). 
person(ford). ini(ford, 8). dest(ford, 4). 
person(fred). ini(fred, 9). dest(fred, 1). 
person(gino). ini(gino, 4). dest(gino, 2). 
person(gavin). ini(gavin, 9). dest(gavin, 3).
