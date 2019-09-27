#include <stdio.h>
void insertionSort(int a[], int lo, int hi)
{
   int i, j, val;
   for (i = lo+1; i <= hi; i++) {
      val = a[i];
      for (j = i; j > lo; j--) {
         if (val >= a[j-1] ) break;
         a[j] = a[j-1];
      }
      a[j] = val;
   }
}
int main()
{
    int a[100];
    for(int i = 0; i < 100; i++)
    {
        a[i] = 100-i;
    }
    insertionSort(a, 0, 99);
    for(int i = 0; i < 100; i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n");
    printf("\n");
    printf("\n");
    return 0;
}