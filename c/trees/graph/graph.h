#ifndef _GRAPH_H_
#define _GRAPH_H_

typedef struct graphnode GraphNode;
typedef struct graphedge GraphEdge;
typedef struct graph Graph;
typedef int(*GraphNodeForEach)(GraphNode *node, void *udata);

GraphNode *GraphNode_New(const char *label, void *data);
char *GraphNode_GetLabel(GraphNode *node);
void GraphNode_AddNeighbor(GraphNode *node, GraphNode *neighbor);

/* HashTable wrappers */
Graph *Graph_New();
void Graph_InsertNode(Graph *This, GraphNode *node);

void Graph_Print(Graph *This);
void Graph_PrintAdjList(Graph *This);
int Graph_BFS(Graph *This, const char *startLbl, GraphNodeForEach cb, void *udata);

#endif // !_GRAPH_H
