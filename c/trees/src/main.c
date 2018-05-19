#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "btree/btree.h"
#include "graph/graph.h"

static void btree__test();
static void graph__test1();
static int testgraph__find_conection(const char *label, void *data, void *udata);

int main()
{
    btree__test();
    graph__test1();
    getchar();
    return 0;
}

static void btree__test()
{
    int i = 0;
    int val[] = { 50, 30, 20, 10, 40, 80, 70, 60, 90, 85, 100 };
    BTreeNode *btree = BTree_NewNode(&val[0], sizeof(int));
    BTreeNode *n1 = BTree_InsertLeft(btree, &val[1], sizeof(int));
    BTreeNode *n2 = BTree_InsertLeft(n1, &val[2], sizeof(int));
    BTreeNode *n3 = BTree_InsertLeft(n2, &val[3], sizeof(int));
    BTreeNode *n4 = BTree_InsertRight(n1, &val[4], sizeof(int));
    BTreeNode *n5 = BTree_InsertLeft(n4, &val[5], sizeof(int));
    BTreeNode *n6 = BTree_InsertLeft(n5, &val[6], sizeof(int));
    BTreeNode *n7 = BTree_InsertLeft(n6, &val[7], sizeof(int));
    BTreeNode *n8 = BTree_InsertRight(n5, &val[8], sizeof(int));
    BTreeNode *n9 = BTree_InsertLeft(n8, &val[9], sizeof(int));
    BTreeNode *n10 = BTree_InsertRight(n8, &val[10], sizeof(int));
    BTree_PrintPreorderInt(btree);
}

static void graph__test1()
{
    char *s1 = "a";
    char *s2 = "c";
    GraphNode *a = GraphNode_New("a", NULL);
    GraphNode *b = GraphNode_New("b", NULL);
    GraphNode *c = GraphNode_New("c", NULL);
    GraphNode *d = GraphNode_New("d", NULL);

    GraphNode_AddNeighbor(a, b);
    GraphNode_AddNeighbor(b, a);
    GraphNode_AddNeighbor(b, c);
    GraphNode_AddNeighbor(c, b);

    Graph *graph = Graph_New();
    Graph_InsertNode(graph, a);
    Graph_InsertNode(graph, b);
    Graph_InsertNode(graph, c);
    Graph_InsertNode(graph, d);

    printf("Graph test ... \n");
    printf("Print all ... \n");
    Graph_Print(graph);
    printf("\n");
    printf("Print adjacency list ... \n");
    Graph_PrintAdjList(graph);
    printf("\n");
    int completed = Graph_BFS(graph, s1, testgraph__find_conection, s2);
    if (completed)
    {
        printf("No connection found  between %s and %s", s1, s2);
    }
}

static int testgraph__find_conection(const char *label, void *data, void *udata)
{
    if(0 == strcmp(label, (char *)udata))
    {
        printf("b <---> %s", label);
        return 1;
    }
    return 0;
}