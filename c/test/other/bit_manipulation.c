#include <stdio.h>
#include <stdlib.h>

#define BIT_CHECK(a,b)      ( (a) & (1 << (b)) )

static int nBits(int n, int bit);
static int *countOnes(int n, int *resultCount);

int main()
{
    printf("Bit %d is %d\n", 4, nBits(77, 4));

    int i = 0;
    int cnt = 0;
    int *res = countOnes(161, &cnt);
    for (; i < cnt; ++i)
    {
        printf("%d\n", res[i]);
    }

    return 0;
}

static int nBits(int n, int bit)
{
    return (BIT_CHECK(n, bit - 1)) > 1;
}

static int *countOnes(int n, int *resultCount)
{
    int count = 0;
    int *res = calloc(1, sizeof(int));
    int i = sizeof(int) * 8;
    for(; i > 0; --i, n = n << 1)
    {
        if(n & 1)
        {
            count += 1;
            res = realloc(res, (count + 1) * sizeof(int));
            res[count] = i;
        }
    }


    res[0] = count;
    *resultCount = count + 1;
    return res;
}