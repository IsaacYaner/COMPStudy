#define MutexDontCare
#include "critical2.h"

byte b[2] = {0,0};

active proctype funcP()
{
    do
        :: true ->
            // bulk code
            // 
            printf("non-critical session P\n");
            b[0] = 1;

            waitp: do
            :: b[1] == 1 ->
                b[0] = 1;
                if 
                :: b[0] == 1 ->
                    b[0] == 1;
                    b[0] = 1;
                :: else -> skip
                fi
            :: else ->
                break;
            od;

            csp: printf("critical session P\n");
            b[0] = 0;
    od;
}

active proctype funcQ()
{
    do
        :: true ->
            // bulk code
            // 
            printf("non-critical session Q\n");
            b[1] = 1;

            waitq: do
                :: b[0] == 1 ->
                b[1] = 0;
                b[0] == 0
                b[1] = 1;
                :: else ->
                    break;
            od;

            csq: printf("critical session Q\n");
            b[1] = 0;
    od;
}

init { run P(); run Q();}

ltl mutex {[]!(P@csp && Q@csq)}
ltl waitp {[] (P@waitp implies (eventually P@csp))}
ltl waitq {[] (Q@waitq implies (<> Q@csq))}
