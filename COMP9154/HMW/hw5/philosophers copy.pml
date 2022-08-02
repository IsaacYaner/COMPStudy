#define N 5

chan forks[N] = [0] of { bit };
chan turn[N] = [0] of { bit };

inline think() {
  do
  :: true -> skip;
  :: true -> break;
  od
}

proctype philosopher(byte i) {
  do
  :: think();
     // pattern matching
     // receive the first message in the queue
     // but only if it equals true
    //  turn[i] ? true;
    if
    :: (i % 2 == 1)
     forks[i] ? true;
     forks[(i + 1) % N] ? true;
    :: else
     forks[(i + 1) % N] ? true;
     forks[i] ? true;
    fi
     // eat
    //  turn[(i + 1) % N] ! true;
     forks[i] ! true;
     forks[(i + 1) % N] ! true;
  od
}

// proctype fork(byte i) {
//   do
//   :: forks[i] ! true;
//      forks[i] ? true;
//   od
// }

init {
  byte i = 1;
  // run bucket();
  for(i : 1 .. N) {
    run philosopher(i-1);
    // run fork(i-1);
  }
  // turn[1] ! true;
  // forks[1] ! true;
  // forks[2] ! true;
}