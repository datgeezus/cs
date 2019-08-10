/*
You have a 2D binary matrix that's filled with 0s and 1s. In the matrix, find the largest square that contains only 1s and return its area.

Example

For

matrix = [
    ['1', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0'],
    ['1', '0', '0', '1', '0']
]
the output should be
maximalSquare(matrix) = 9.


 */

#include <stdio.h>
#include <stdlib.h>

#define MAX(a,b) ( ( (a) >= (b) ) ? (a) : (b) )
#define MIN(a,b) ( ( (a) <= (b) ) ? (a) : (b) )

static char test[5][5] =
{
    { 1, 0, 1, 1 ,1 },
    { 1, 0, 1, 1 ,1 },
    { 1, 1, 1, 1 ,1 },
    { 1, 0, 0, 1 ,0 },
    { 1, 0, 0, 1 ,0 }
};

static int max_square(char matrix[][5]);

int main()
{
    printf("max: %d\n", max_square(test));
    getchar();
    return 0;
}

static int max_square(char matrix[][5])
{
    int max = 0;
    
    
    int i, j = 0;
    for(i = 0; i < 5; ++i)
    {
        for(j = 0; j < 5; ++j)
        {
            if((i == 0) || (j == 0))
            {
                max = MAX(matrix[i][j], max);
            }
            else
            {
                if(matrix[i][j])
                {
                    char mem[3] =
                        {
                            matrix[i - 1][j - 1],
                            matrix[i][j - 1],
                            matrix[i - 1][j]};
                    matrix[i][j] = MIN(MIN(mem[0], mem[1]), mem[2]) + 1;
                    max = MAX(matrix[i][j], max);
                }
            }
        }
    }

    return max * max;
}