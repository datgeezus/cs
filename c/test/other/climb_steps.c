#include<stdio.h>
#include<stdlib.h>

static int tests[] = { 1, 2, 26, 38, 28};


static int climbStairs(int n);
static int climbStairsNoMem(int n);

int main()
{
    int i = 0;
    for(; i < 5; ++i)
    {
        printf("n:%d, s:%d\n", tests[i], climbStairs(tests[i]));
        printf("n:%d, s:%d\n", tests[i], climbStairsNoMem(tests[i]));
    }
    getchar();
    return 0;
}

static int climbStairs(int n)
{
    int *cache = calloc(n+1, sizeof(int));
    int i;

    cache[0] = 1;
    cache[1] = 1;
    cache[2] = 2;
    for(i = 3; i < n+1; ++i)
    {
        cache[i] = cache[i - 1] + cache[i - 2];
    }

    return cache[n];
}

static int climbStairsNoMem(int n)
{
    int cache[2] = { 0 , 0 };
    int i;

    if(n == 1)
    {
        return 1;
    }

    cache[0] = 1;
    cache[1] = 2;
    for(i = 2; i < n; ++i)
    {
        int curr = cache[0] + cache[1];
        cache[0] = cache[1];
        cache[1] = curr;
    }

    return cache[1];
}