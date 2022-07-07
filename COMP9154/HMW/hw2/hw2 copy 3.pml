#define MutexDontCare
#include "critical2.h"

bit wantp = 0;
bit wantq = 0;
bit wantr = 0;
bit turn = 0;

proctype P() {
    do
    :: non_critical_section();
        waitp: wantp = true

        do
        :: wantq -> 
            if
            :: turn != 0 -> 
                    wantp = false;
                    turn == 2;
                    wantp = true;
            :: else -> skip
            fi
        :: else -> break
        od

        do
        :: wantr -> 
            if
            :: turn == 2 -> 
                    wantp = false;
                    turn == 0;
                    wantp = true;
            :: else -> skip
            fi
        :: else -> break
        od

        csp: critical_section();
        turn = 1;
        wantp = false;
    od
}

proctype Q() {
    do
    :: non_critical_section();
        waitq: wantq = true

        do
        :: wantr -> 
            if
            :: turn != 1 -> 
                wantq = false;
                turn == 0;
                wantq = true;
            :: else -> skip
            fi
        :: else -> break
        od

        do
        :: wantp -> 
            if
            :: turn == 0 -> 
                wantq = false;
                turn == 1;
                wantq = true;
            :: else -> skip
            fi
        :: else -> break
        od

        csq: critical_section();
            turn = 2;
            wantq = false;
    od
}

proctype R() {
    do
    :: non_critical_section();
        waitr: wantr = true
        
        do
        :: wantp -> 
            if
            :: turn != 2 -> 
                wantr = false;
                turn == 1;
                wantr = true;
            :: else -> skip
            fi
        :: else -> break
        od

        do
        :: wantq -> 
            if
            :: turn == 1 -> 
                wantr = false;
                turn == 2;
                wantr = true;
            :: else -> skip
            fi
        :: else -> break
        od

        csr: critical_section();
            turn = 0;
            wantr = false;
    od
}

init { run P(); run Q(); run R();}

ltl mutex { [] (!(P@csp && Q@csq) && !(P@csp && R@csr) && !(R@csr && Q@csq))}
ltl waitp { [] (P@waitp implies (eventually P@csp))  }
ltl waitq { [] (Q@waitq implies (<> Q@csq))  }
ltl waitr { [] (R@waitr implies (<> R@csr))  }