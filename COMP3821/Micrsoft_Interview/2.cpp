#include <stdio.h>

/*
    An array of integers (positive and negative) is given, 
    each having at most K bits (plus the sign bit), 
    and it is known that the sum of all the integers in the array also has at most K bits (plus the sign bit). 
    Design an algorithm that computes the sum of integers in the array, 
    with all intermediate sums also having at most K bits (plus the sign bit). 
    [Hint: find in what order you should add positive and negative numbers].
*/

//????????????????????????????????
//Could I just use what is considered in basic add or reduce?
//use mod 2<<K to yeild the correct answer
//If K-1(because sign bit counts) bit is at least 1
//  and add two numbers with truncated K-1 bit to yield totally(plus original numbers)
//  at least two 1s, then cut two 1s by cutting one 1 and add up, and then ans-=2<<K-1.
//  i.e. 11010101010001 = a
//  and  01001010101001 = b
//  then 10011111111010 = c = (a-2<<K-1)+b
//  and 100011111111010 = a+b
//  because there are two 1s in a and c
//  so we first cut a's 1 and then cut c's 1
//  to get answer
//????????????????????????????????



int main()
{
    
    return 0;
}