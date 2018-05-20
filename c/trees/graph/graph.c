#include "graph.h"
#include "hashtable/hashtable.h"
#include "queue/queue.h"
#include "stack/stack.h"
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
    GraphNode *node;
    Queue *visit;
    HashTable *visited;
};

struct dfsdata
{
    Graph *graph;
    GraphNode *node;
    Stack *visit;
    HashTable *visited;
};

struct bfspathdata
{
    GraphNode *start;
    GraphNode *end;
};

static int graph__bfs(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata, HashTable **path);
static int graph__dfs(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata, HashTable **path);
static const char **graph__reconstruct_path(HashTable *path, GraphNode *start, GraphNode *end);
static int graph__foreach_path(GraphNode *node, void *udata);
static int graph__foreach_print(GraphNode *node, void *udata);
static void graph__foreach_pprint(const char *label, void *udata);
static void graph__bfs_hashset_foreach(const char *key, void *udata);
static void graph__dfs_hashset_foreach(const char *key, void *udata);

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

void *GraphNode_GetData(GraphNode *node)
{
    return node->data;
}

void GraphNode_AddNeighbor(GraphNode *node, GraphNode *neighbor)
{
    if (NULL != node && NULL != neighbor)
    {
        const char *label = GraphNode_GetLabel(neighbor);
        HashSet_Insert(node->neighbors, label);
    }
}

int Graph_Print(GraphNode *node, void *udata)
{
    return graph__foreach_print(node, udata);
}

void Graph_PrintAdjList(Graph *This)
{
    HashSet_ForEach(This->keys, graph__foreach_pprint, This);
}

int Graph_BFS(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata)
{
    HashTable *dummy;
    return graph__bfs(This, start, cb, udata, &dummy);
}

int Graph_DFS(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata)
{
    HashTable *dummy;
    return graph__dfs(This, start, cb, udata, &dummy);
}

char **Graph_FindPath(Graph *This, GraphNode *start, GraphNode *end)
{
    char **_path = NULL;
    HashTable *path;
    struct bfspathdata data = { start, end };

    int completed = graph__bfs(This, start, graph__foreach_path, &data, &path);
    if (!completed)
    {
        /* found path, reconstruct it */
        _path = graph__reconstruct_path(path, start, end);
    }

    return _path;
}

static int graph__bfs(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata, HashTable **path)
{
    int completed = 1;
    Queue *visit = Queue_New();
    HashTable *visited = HashTable_New();
    (*path) = visited;
    struct bfsdata data = { This, NULL, visit, (*path) };

    Queue_EnqueuePtr(visit, (void *)start);
    HashTable_InsertPtr(visited, start->label, NULL);

    while (!Queue_IsEmpty(visit))
    {
        GraphNode *node = Queue_DequePtr(visit);

        int exit = cb(node, udata);
        if (1 == exit)
        {
            completed = 0;
            break;
        }

        data.node = node;
        HashSet_ForEach(node->neighbors, graph__bfs_hashset_foreach, (void *)&data);
    }

    return completed;
}

static void graph__bfs_hashset_foreach(const char *key, void *udata)
{
    struct bfsdata *data = (struct bfsdata *)udata;
    GraphNode *neighbor = HashTable_Find(data->graph->table, key);
    if(!HashTable_In(data->visited, key))
    {
        Queue_EnqueuePtr(data->visit, neighbor);
        HashTable_InsertPtr(data->visited, neighbor->label, data->node);
    }
}

static int graph__dfs(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata, HashTable **path)
{
    int completed = 1;
    Stack *visit = Stack_New();
    HashTable *visited = HashTable_New();
    (*path) = visited;
    struct dfsdata data = { This, NULL, visit, (*path) };

    Stack_PushPtr(visit, start);
    HashTable_InsertPtr(visited, start->label, NULL);
    while (!Stack_IsEmpty(visit))
    {
        GraphNode *node = (GraphNode *)Stack_PopPtr(visit);
        int exit = cb(node, udata);
        if (1 == exit)
        {
            completed = 0;
            break;
        }
        else
        {
            data.node = node;
            HashSet_ForEach(node->neighbors, graph__dfs_hashset_foreach, (void *)&data);
        }
    }
}

static void graph__dfs_hashset_foreach(const char *key, void *udata)
{
    struct dfsdata *data = (struct dfsdata *)udata;
    GraphNode *neighbor = HashTable_Find(data->graph->table, key);
    if(!HashTable_In(data->visited, key))
    {
        Stack_PushPtr(data->visit, neighbor);
        HashTable_InsertPtr(data->visited, neighbor->label, data->node);
    }
}

static int graph__foreach_print(GraphNode *node, void *udata)
{
    printf("(%s) ", node->label);
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

static int graph__foreach_path(GraphNode *node, void *udata)
{
    int exit = 0;
    struct bfspathdata *data = (struct bfsdata *)udata;
    if (0 == strcmp(node->label, data->end->label))
    {
        exit = 1;
    }

    return exit;
}

static const char **graph__reconstruct_path(HashTable *path, GraphNode *start, GraphNode *end)
{
    char **shortestPath = NULL;
    size_t i = 0;
    size_t n = 0;   /* size of output array */
    GraphNode *node = NULL;
    for (n = 0, node = end; NULL != node; ++n)
    {
        node = HashTable_Find(path, node->label);
    }

    shortestPath = calloc(n, sizeof(const char *));

    i = n - 1;
    node = end;
    for (i = n - 1, node = end; NULL != node; --i)
    {
        shortestPath[i] = node->label;
        node = HashTable_Find(path, node->label);
    }

    return shortestPath;
}
