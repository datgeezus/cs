#include "queue/queue.h"
#include "stack/stack.h"
#define ROW 9 
#define COL 10 

typedef struct Point Point;

//To store matrix cell cordinates 
struct Point 
{ 
    int r; 
    int c; 
    char move;
}; 
  
// A Data Structure for queue used in BFS 
struct queueNode 
{ 
    Point pt;  // The cordinates of a cell 
    int dist;  // cell's distance of from the source 
}; 

static int ROWIDX[] = { -1, 1,  0, 0 };
static int COLIDX[] = {  0, 0, -1, 1 };
static char MOVES[] = { 'U', 'D', 'L', 'R' };
static int mat[ROW][COL] = 
    { 
        { 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
        { 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
        { 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
        { 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 }, 
        { 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 }, 
        { 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 }, 
        { 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 }, 
        { 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 }, 
        { 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 } 
    }; 
  

static int isValid(int r, int c);
static Queue * shortest_path_in_maze();

int main()
{
    Queue *path = shortest_path_in_maze();
    int i, j = 0;
    for(i = 0; i < ROW; ++i)
    {
        for(j = 0; j < COL; ++j)
        {
            printf("[%d]", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    while(!Queue_IsEmpty(path))
    {
        Point *point = Queue_DequePtr(path);
        printf("[%d][%d] -> ", point->r, point->c);
    }
    printf("|\n");

    getchar();
    return 0;
}

static Queue * shortest_path_in_maze()
{
    Point source = {0, 0, 'S'}; 
    Point dest = {8, 1, 'D'}; 

    /* BFS */
    Queue *path = Queue_New();

    Queue_EnqueuePtr(path, &source);
    mat[source.r][source.c] = 4;

    while(!Queue_IsEmpty(path))
    {
        Point *curr = (Point *)Queue_DequePtr(path);
        if((curr->r == dest.r) && (curr->c == dest.c))
        {
            mat[curr->r][curr->c] = 4;
            break;
        }
        else
        {
            int i = 0;
            mat[curr->r][curr->c] = 2;
            for(; i < 4; ++i)
            {
                int nextc = curr->c + COLIDX[i];
                int nextr = curr->r + ROWIDX[i];
                if(isValid(nextr, nextc))
                {
                    Point *new = malloc(sizeof(Point));
                    new->c = nextc;
                    new->r = nextr;
                    new->move = MOVES[i];
                    Queue_EnqueuePtr(path, new);
                }
                // mat[curr->r][curr->c] = tmp;
            }
        }
    }

    return path;
}

static int isValid(int r, int c)
{
    return (c >= 0)
        && (c < COL)
        && (r >= 0)
        && (r < ROW)
        && (mat[r][c] == 1);
}