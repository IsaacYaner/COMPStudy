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
    forks[2] ! true;

    forks[2] ? true;
    forks[1] ? true;
  od;
}

proctype philosopher2() {
  do
  :: think();
    forks[2] ? true;

    forks[2] ! true;
    forks[3] ! true;

    forks[3] ? true;
  od;
}

proctype philosopher3() {
  do
  :: think();
    forks[3] ? true;

    forks[3] ! true;
    forks[4] ! true;

    forks[4] ? true;
  od;
}

proctype philosopher4() {
  do
  :: think();
    forks[4] ? true;

    forks[4] ! true;
    forks[5] ! true;

    forks[5] ? true;
  od;
}

proctype philosopher5() {
  do
  :: think();
    forks[1] ? true;
    forks[5] ? true;

    forks[1] ! true;
    forks[5] ! true;

  od;
}

init {
  //Phil 1 start firstly, assuming that they has got two forks
  run philosopher1();
  run philosopher2();
  run philosopher3();
  run philosopher4();
  run philosopher5();
}