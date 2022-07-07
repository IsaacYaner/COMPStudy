#define MutexDontCare
#include "critical2.h"

bit b[2] = {0,0};

proctype P()
{
    do
    :: non_critical_section();
        waitp: b[0] = true;

        do
        :: b[1] == true ->
            b[0] = true;
            b[0] == true;
            b[0] = true;
        :: else ->
            break;
        od;

        csp: critical_section();
        b[0] = false;
    od;
}

proctype Q()
{
    do
    :: non_critical_section();
        waitq: b[1] = true;

        do
        :: b[0] == true ->
            b[1] = false;
            b[0] == false;
            b[1] = true;
        :: else ->
            break;
        od;

        csq: critical_section();
        b[1] = false;
    od;
}

init { run P(); run Q();}

// Mutual exclusion -- works
ltl mutex {[]!(P@csp && Q@csq)}

// Eventually entry
ltl waitp {[] (P@waitp implies (eventually P@csp))}
// Oops! -- Q may wait for p forever
ltl waitq {[] (Q@waitq implies (<> Q@csq))}

// Absence of deadlock -- works
// Selected in options under 'Safety' tab
// Absence of unnecessary delay -- works
ltl absp {[]((([] !Q@csq) && P@waitp) implies (<> P@csp))}
ltl absq {[]((([] !P@csp) && Q@waitq) implies (<> Q@csq))}
