#ifndef _GRAPH_H_
#define _GRAPH_H_

typedef struct graphnode GraphNode;
typedef struct graphedge GraphEdge;
typedef struct graph Graph;
typedef int(*GraphNodeForEach)(GraphNode *node, void *udata);

GraphNode *GraphNode_New(const char *label, void *data);
char *GraphNode_GetLabel(GraphNode *node);
void *GraphNode_GetData(GraphNode *node);
void GraphNode_AddNeighbor(GraphNode *node, GraphNode *neighbor);

/* HashTable wrappers */
Graph *Graph_New();
void Graph_InsertNode(Graph *This, GraphNode *node);

int Graph_Print(GraphNode *node, void *udata);
void Graph_PrintAdjList(Graph *This);
int Graph_BFS(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata);
int Graph_DFS(Graph *This, GraphNode *start, GraphNodeForEach cb, void *udata);
char **Graph_FindPath(Graph *This, GraphNode *start, GraphNode *end);

#endif // !_GRAPH_H
