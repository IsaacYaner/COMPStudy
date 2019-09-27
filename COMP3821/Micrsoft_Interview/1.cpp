#include <stdio.h>


/*
Given an array of real numbers A[1..n], 
find a contiguous sub - array A[i..j], 1 ¡Ü  i ¡Ü  j ¡Ü  n, with the largest sum.
Note that the array might contain both positive and negative numbers.
[Hint:Dynamic Programming(or similar)]
*/

#define max(a, b) a>b?a:b

int main()
{
	int n = 0;
	scanf("%d", &n);
	int arr[n];
	int sum[n];
	int left[n];
	for (int i = 0; i < n; i++)
	{
		scanf("%d", arr+i);
		sum[i] = arr[i];
		left[i] = i;
	}
	int maxim = arr[0];
	int subL = 0;
	int subR = 0;
	for (int i = 1; i < n; i++)
	{
		sum[i] = max(sum[i-1]+arr[i], sum[i]);
		if (sum[i] - arr[i])
		{
			left[i] = left[i - 1];
		}
		if (sum[i] > maxim)
		{
			maxim = sum[i];
			subL = left[i];
			subR = i;
		}
	}
	for (int i = 0; i < n; i++)
	{
		printf("%d ",sum[i]);
	}
	subL++;
	subR++;
	printf("\nLargest sum is %d, with i=%d and j=%d", maxim, subL, subR);
	return 0;
}