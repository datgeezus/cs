/*

Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

Example:
Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4
The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]

*/

#include <stdio.h>

#define MAX(a,b) ( ((a) > (b)) ? (a) : (b) )

struct test
{
    int val[10];
};

static struct test test[] = 
{ 
    {1, 3, 5, 3, 1, 3, 1, 5, 3, 1 },
    {1, 3, 5, 3, 1, 3, 1, 3, 3, 1 },
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
    {1, 3, 1, 3, 1, 3, 1, 3, 1, 3 },
    {1, 3, 1, 5, 1, 3, 1, 5, 1, 3 },
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 0 }
};


static int findSequence(int *arr, int n);

int main()
{
    int i = 0;
    for(; i < 6; ++i)
    {
        printf("%d\n", findSequence(test[i].val, 10));
    }
    getchar();
    return 0;
}

static int findSequence(int *arr, int n)
{
    if(n <= 1)
    {
        /* we  need at least 2 numbers */
        return 0;
    }

    int i = 2;
    int max = 0;
    int mem = 2;
    if(arr[0] != arr[1])
    {
        /* for n=2 the max would be a secuence of 2, if the values are different */
        max = 2;
    }

    for(i = 2; i < n; ++i)
    {
        if((arr[i] == arr[i-2]) && (arr[i] != arr[i-1]))
        {
            mem += 1;
            max = MAX(max, mem);
        }
        else
        {
            /* sequence broken, reset to minimum */
            mem = 2;
        }
    }

    return max;
}