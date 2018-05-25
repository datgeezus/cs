#include "btree/btree.h"

#include <stdio.h>

static BTreeNode *node[10] = { NULL };
static int data[] = { 0, 1, 2, 3, 4, 5, 6 ,7 ,8, 9 };

struct bsnodepaiar
{
    BTreeNode *node;
    size_t depth;
};

struct bsdata
{
    struct bsnodepaiar pair;
};

static int btree__foreach(BTreeNode *node, const void *udata);

void pset_balanced_binary_tree()
{
    int lval = -100000000;
    int val[] = { 50, 30, 20, 10, 40, 80, 70, 60, 90, 85, 100 };
    BTreeNode *root = BTree_NewNode(&val[0], sizeof(int));
    BTreeNode *n1 = BTree_InsertLeft(root, &val[1], sizeof(int));
    BTreeNode *n2 = BTree_InsertLeft(n1, &val[2], sizeof(int));
    BTreeNode *n3 = BTree_InsertLeft(n2, &val[3], sizeof(int));
    BTreeNode *n4 = BTree_InsertRight(n1, &val[4], sizeof(int));
    BTreeNode *n5 = BTree_InsertRight(root, &val[5], sizeof(int));
    BTreeNode *n6 = BTree_InsertLeft(n5, &val[6], sizeof(int));
    BTreeNode *n7 = BTree_InsertLeft(n6, &val[7], sizeof(int));
    BTreeNode *n8 = BTree_InsertRight(n5, &val[8], sizeof(int));
    BTreeNode *n9 = BTree_InsertLeft(n8, &val[9], sizeof(int));
    BTreeNode *n10 = BTree_InsertRight(n8, &val[10], sizeof(int));

    int completed = BTree_DFS_Inorder(root, btree__foreach, &lval);
    if (1 == completed)
    {
        printf("Valid binary search tree\n");
    }
    else
    {
        printf("Not Valid binary search tree\n");
    }
}

static int btree__foreach(BTreeNode *node, const void *udata)
{
    int v = *(int *)BTree_GetData(node);
    int u = *(int *)udata;
    return !(v > u);
}