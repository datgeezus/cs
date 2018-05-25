#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(a, b)   ( (a) > (b)  ? (a) : (b) )

typedef struct
{
    size_t weight;
    long long value;
} Cake;

const Cake cakes[] =
{
    {7, 160},
    {3, 90},
    {2, 15},
};

static int **C = { NULL };
static long long max_knapsack(Cake cakes[], size_t n, size_t capacity);
static long long max_knapsack_rec(Cake cakes[], size_t n, size_t capacity);
static long long max_knapsack_bup(Cake cakes[], size_t n, size_t capacity);
static long long max_unbounded_knapsack_bup(Cake cakes[], size_t n, size_t capacity);

void pset_cake_thief()
{
    max_knapsack(cakes, 3, 20);
}

static long long max_knapsack(Cake cakes[], size_t n, size_t capacity)
{
    size_t i, j;
    C = calloc(n + 1, sizeof(int *));
    for (i = 0; i < n + 1; ++i)
    {
        C[i] = calloc(capacity + 1, sizeof(int));
    }

    for (i = 0; i < n + 1; ++i)
    {
        for (j = 0; j < capacity + 1; ++j)
        {
            C[i][j] = -1;
        }
    }

    long long v = max_knapsack_rec(cakes, 3, capacity);
    printf("v: %d\n", v);
    v = max_knapsack_bup(cakes, 3, capacity);
    printf("v: %d\n", v);
}

static long long max_knapsack_rec(Cake cakes[], size_t n, size_t c)
{
    /* DP(i, C) = max(PD(i + 1, C), v[i] + DP(i + 1, C - c[i])) */
    long long res = 0;
    if (-1 != C[n][c])
    {
        return C[n][c];
    }
    else
    {
        if (0 == n || 0 == c)
        {
            res = 0;
        }
        else if (cakes[n].weight > c)
        {
            res = max_knapsack_rec(cakes, n - 1, c);
        }
        else
        {
            long long tmp1 = max_knapsack_rec(cakes, n - 1, c);
            long long tmp2 = cakes[n].value + max_knapsack_rec(cakes, n - 1, c - cakes[n].weight);
            res = MAX(tmp1, tmp2);
        }
    }

    C[n][c] = res;
    return res;
}

static long long max_knapsack_bup(Cake cakes[], size_t n, size_t capacity)
{
    /* C[i, j] = max(C[i + 1, j], v[i] + C[i + 1, j - S[i]]) */
    int i = 0;
    int w = 0;

    for (i = 0; i < n; ++i)
    {
        for (w = 0; w <= capacity; ++w)
        {
            if (0 == i || 0 == w)
            {
                C[i][w] = 0;
            }
            else if (cakes[i].weight > w)
            {
                C[i][w] = C[i - 1][w];
            }
            else
            {
                long long tmp1 = C[i - 1, w];
                long long tmp2 = cakes[i].value + C[i - 1, w - cakes[i].weight];
                C[i][w] = MAX(tmp1, tmp2);
            }
        }
    }

    return C[n][capacity];
}

static long long max_unbounded_knapsack_bup(Cake cakes[], size_t n, size_t capacity)
{
    size_t currCap = 0;
    long long *maxVatC = calloc(capacity + 1, sizeof(long long));
    for (currCap = 0; currCap <= capacity; ++currCap)
    {
        size_t i = 0;
        long long currMaxV = 0;

        for (i = 0; i < n; ++i)
        {
            Cake cake = cakes[i];
            if (0 == cake.weight)
            {
                break;
            }

            if (cake.weight <= currCap)
            {
                long long maxV = cake.value + maxVatC[currCap - cake.weight];
                currMaxV = MAX(maxV, currMaxV);
            }
        }
        maxVatC[currCap] = currMaxV;
    }

    return maxVatC[capacity];
}
