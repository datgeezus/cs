#include "queue/queue.h"
#include "stack/stack.h"
#include "linkedlist/linkedlist.h"
#define ROW 9 
#define COL 10 

typedef struct Point Point;

//To store matrix cell cordinates 
struct Point 
{ 
    int r; 
    int c; 
    LinkedList *path;
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
static Stack * shortest_path_in_maze();

int main()
{
    Stack *path = shortest_path_in_maze();
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

    while(!Stack_IsEmpty(path))
    {
        Point *point = Stack_PopPtr(path);
        printf("[%d][%d] -> ", point->r, point->c);
    }
    printf("|\n");

    getchar();
    return 0;
}

static Stack * shortest_path_in_maze()
{
    Point source = {0, 0, LinkedList_New()}; 
    Point dest = {8, 1, LinkedList_New()}; 

    /* BFS */
    Queue *visit = Queue_New();
    Stack *path = Stack_New();

    Queue_EnqueuePtr(visit, &source);
    Stack_PushPtr(path, &source);
    mat[source.r][source.c] = 4;

    while(!Queue_IsEmpty(visit))
    {
        Point *curr = (Point *)Queue_DequePtr(visit);
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
                    LinkedList_Append(new->path, &MOVES[i], 2);
                    Queue_EnqueuePtr(visit, new);
                    Stack_PushPtr(path, new);
                }
            }
            // Stack_PopPtr(path);
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