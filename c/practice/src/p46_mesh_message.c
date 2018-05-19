#include "graph/graph.h"
#include "hashtable/hashtable.h"
#include <stdio.h>

static GraphNode *start = NULL;
static GraphNode *end = NULL;
static GraphNode *Min = NULL;
static GraphNode *William = NULL;
static GraphNode *Jayden = NULL;
static GraphNode *Ren = NULL;
static GraphNode *Amelia = NULL;
static GraphNode *Miguel = NULL;
static GraphNode *Adam = NULL;
static GraphNode *Noam = NULL;
static GraphNode *Omar = NULL;
static GraphNode *Sofia = NULL;
static GraphNode *Lucas = NULL;
static GraphNode *Nathan = NULL;
static GraphNode *Liam = NULL;
static GraphNode *Scott = NULL;


static Graph * graph__setup();

struct bfsdata
{
    char *end;
    HashTable *path;
} data;

void pset__mesh_message(void)
{
    Graph *graph = graph__setup();
    Graph_PrintAdjList(graph);

    start = Miguel;
    end = Adam;
    char **path = Graph_FindPath(graph, start, end);
    printf("%s", path[0]);
}

static Graph * graph__setup()
{
    Graph *graph = Graph_New();
    Min = GraphNode_New("Min", NULL);
    William = GraphNode_New("William", NULL);
    Jayden = GraphNode_New("Jayden", NULL);
    Ren = GraphNode_New("Ren", NULL);
    Amelia = GraphNode_New("Amelia", NULL);
    Miguel = GraphNode_New("Miguel", NULL);
    Adam = GraphNode_New("Adam", NULL);
    Noam = GraphNode_New("Noam", NULL);
    Omar = GraphNode_New("Omar", NULL);
    Sofia = GraphNode_New("Sofia", NULL);
    Lucas = GraphNode_New("Lucas", NULL);
    Nathan = GraphNode_New("Nathan", NULL);
    Liam = GraphNode_New("Liam", NULL);
    Scott = GraphNode_New("Scott", NULL);

    GraphNode_AddNeighbor(Min, William);
    GraphNode_AddNeighbor(Min, Jayden);
    GraphNode_AddNeighbor(Min, Omar);

    GraphNode_AddNeighbor(William, Min);
    GraphNode_AddNeighbor(William, Noam);

    GraphNode_AddNeighbor(Jayden, Min);
    GraphNode_AddNeighbor(Jayden, Amelia);
    GraphNode_AddNeighbor(Jayden, Ren);
    GraphNode_AddNeighbor(Jayden, Noam);

    GraphNode_AddNeighbor(Ren, Jayden);
    GraphNode_AddNeighbor(Ren, Omar);

    GraphNode_AddNeighbor(Amelia, Jayden);
    GraphNode_AddNeighbor(Amelia, Adam);
    GraphNode_AddNeighbor(Amelia, Miguel);

    GraphNode_AddNeighbor(Adam, Amelia);
    GraphNode_AddNeighbor(Adam, Miguel);
    GraphNode_AddNeighbor(Adam, Sofia);
    GraphNode_AddNeighbor(Adam, Lucas);

    GraphNode_AddNeighbor(Miguel, Amelia);
    GraphNode_AddNeighbor(Miguel, Adam);
    GraphNode_AddNeighbor(Miguel, Liam);
    GraphNode_AddNeighbor(Miguel, Nathan);

    GraphNode_AddNeighbor(Noam, Nathan);
    GraphNode_AddNeighbor(Noam, Jayden);
    GraphNode_AddNeighbor(Noam, William);

    GraphNode_AddNeighbor(Omar, Ren);
    GraphNode_AddNeighbor(Omar, Min);
    GraphNode_AddNeighbor(Omar, Scott);

    Graph_InsertNode(graph, Min);
    Graph_InsertNode(graph, William);
    Graph_InsertNode(graph, Jayden);
    Graph_InsertNode(graph, Ren);
    Graph_InsertNode(graph, Amelia);
    Graph_InsertNode(graph, Miguel);
    Graph_InsertNode(graph, Adam);
    Graph_InsertNode(graph, Noam);
    Graph_InsertNode(graph, Omar);
    Graph_InsertNode(graph, Sofia);
    Graph_InsertNode(graph, Lucas);
    Graph_InsertNode(graph, Nathan);
    Graph_InsertNode(graph, Liam);
    Graph_InsertNode(graph, Scott);

    return graph;
}

