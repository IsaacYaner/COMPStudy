#define N 5

chan forks[N+1] = [0] of { bit };

inline think() {
  do
  :: true -> skip;
  :: true -> break;
  od;
}

proctype philosopher1() {
  do
  :: true->
    think();
    forks[1] ! true;
    forks[2] ? true;
  od;
}

proctype philosopher2() {
  do
  :: think();
    forks[1] ? true;

    forks[2] ! true;
  od;
}

init {
  run philosopher1();
  run philosopher2();
}