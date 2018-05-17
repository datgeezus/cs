#include <stdio.h>
#include <stdlib.h>
#include "btree/btree.h"

static void btree__test();

int main()
{
    btree__test();
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