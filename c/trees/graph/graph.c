#include "graph.h"
#include "hashtable/hashtable.h"
#include "queue/queue.h"
#include "set/set.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct graphnode
{
    char *label;
    void *data;
    HashSet *neighbors;
};

struct graph
{
    HashSet *keys;
    HashTable *table;
};

struct bfsdata
{
    Graph *graph;
    Queue *visit;
    HashSet *visited;
};

static int graph__foreach_print(GraphNode *node, void *udata);
static void graph__foreach_pprint(const char *label, void *udata);
static void graph__bfs_hashset_foreach(const char *key, void *udata);

Graph *Graph_New()
{
    Graph *This = calloc(1, sizeof(Graph));
    This->keys = HashSet_New();
    This->table = HashTable_New();
    return This;
}

void Graph_InsertNode(Graph *This, GraphNode *node)
{
    if (NULL != This)
    {
        HashSet_Insert(This->keys, node->label);
        HashTable_InsertPtr(This->table, node->label, node);
    }
}

GraphNode *GraphNode_New(const char *label, void *data)
{
    GraphNode *This = calloc(1, sizeof(GraphNode));

    This->label = calloc(1, strlen(label) + 1);
    strcpy(This->label, label);
    This->data = data;
    This->neighbors = HashSet_New();

    return This;
}

char *GraphNode_GetLabel(GraphNode *node)
{
    return node->label;
}

void GraphNode_AddNeighbor(GraphNode *node, GraphNode *neighbor)
{
    if (NULL != node && NULL != neighbor)
    {
        const char *label = GraphNode_GetLabel(neighbor);
        HashSet_Insert(node->neighbors, label);
    }
}

void Graph_Print(Graph *This)
{
    Graph_BFS(This, "a", graph__foreach_print, NULL, NULL);
}

void Graph_PrintAdjList(Graph *This)
{
    HashSet_ForEach(This->keys, graph__foreach_pprint, This);
}

int Graph_BFS(Graph *This, const char *startLbl, GraphNodeForEach cb, void *udata)
{
    int completed = 1;
    Queue *visit = Queue_New();
    HashSet *visited = HashSet_New();
    GraphNode *start = HashTable_Find(This->table, startLbl);
    struct bfsdata data = { This, visit, visited };

    Queue_EnqueuePtr(visit, (void *)start);
    HashSet_Insert(visited, start->label);

    while (!Queue_IsEmpty(visit))
    {
        GraphNode *node = Queue_DequePtr(visit);

        int exit = cb(node, udata);
        if (1 == exit)
        {
            completed = 0;
            break;
        }

        HashSet_ForEach(node->neighbors, graph__bfs_hashset_foreach, (void *)&data);
    }

    return completed;
}

static void graph__bfs_hashset_foreach(const char *key, void *udata)
{
    struct bfsdata *data = (struct bfsdata *)udata;
    GraphNode *neighbor = HashTable_Find(data->graph->table, key);
    if(!HashSet_In(data->visited, key))
    {
        HashSet_Insert(data->visited, key);
        Queue_EnqueuePtr(data->visit, neighbor);
    }
}

static int graph__foreach_print(GraphNode *node, void *udata)
{
    printf("(%s) ", GraphNode_GetLabel(node));
    return 0;
}

static void graph__foreach_pprint(const char *label, void *udata)
{
    Graph *graph = (Graph *)udata;
    GraphNode *n = HashTable_Find(graph->table, label);
    printf("{%s: ", label);
    HashSet_Print(n->neighbors);
    printf("}\n");
}
