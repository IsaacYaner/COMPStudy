% 数据部分
#const maxtime = 20.
#const capacity = 2.
floor(1..10).
time(0..maxtime).

% 电梯的初始状态只有pos
lift(a).
pos(0, a, 1).
lift(b).
pos(0, b, 10).

% 人的初始状态只有ini和dest
person(alice). ini(alice, 7). dest(alice, 4).
person(bob). ini(bob, 4). dest(bob, 1). 
person(cathy). ini(cathy, 2). dest(cathy, 5). 
person(david). ini(david, 2). dest(david, 5). 
person(eric). ini(eric, 3). dest(eric, 8). 
person(felix). ini(felix, 10). dest(felix, 1).
person(george). ini(george, 1). dest(george, 10). 
person(helen). ini(helen, 1). dest(helen, 5). 