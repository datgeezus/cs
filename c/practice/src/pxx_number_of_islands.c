#include <stdio.h>

#define ROW 5 
#define COL 5

static int mem[ROW][COL];

static int countIslands(int M[ROW][COL]);
static void DFS(int M[ROW][COL], int row, int col);
static int withinBounds(int M[ROW][COL], int row, int col);

// Driver code 
void number_of_islands() 
{ 
    int M[ROW][COL] = { { 1, 1, 0, 0, 0 }, 
                        { 0, 1, 0, 0, 1 }, 
                        { 1, 0, 0, 1, 1 }, 
                        { 0, 0, 0, 0, 0 }, 
                        { 1, 0, 1, 0, 1 } }; 
  
    printf("Number of islands is: %d\n", countIslands(M)); 
}


static int countIslands(int M[ROW][COL])
{
    int count = 0;
    int i = 0;
    int j = 0;

    for(i = 0; i < ROW; ++i)
    {
        for(j = 0; j < COL; ++j)
        {
            if((1 == M[i][j]) && (0 == mem[i][j]))
            {
                DFS(M, i, j);
                count += 1;
            }
        }
    }

    return count;
}

static void DFS(int M[ROW][COL], int row, int col)
{
    int rowIndex[] = {-1, -1, -1,  0, 0,  1, 1, 1};
    int colIndex[] = {-1,  0,  1, -1, 1, -1, 0, 1};
    int k = 0;

    mem[row][col] = 1;

    for(; k < 8; ++k)
    {
        if(withinBounds(M, row + rowIndex[k], col + colIndex[k]))
        {
            DFS(M, row + rowIndex[k], col + colIndex[k]);
        }
    }
}

static int withinBounds(int M[ROW][COL], int row, int col)
{
    return ((row >= 0) &&
            (row < ROW) &&
            (col >= 0) &&
            (col < COL) &&
            (1 == M[row][col]) &&
            (0 == mem[row][col]));
}