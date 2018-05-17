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
    int val[4] = { 1,2,3,4 };
    BTreeNode *btree = BTree_NewNode(&val[0], sizeof(int));
    BTreeNode *n1 = BTree_InsertLeft(btree, &val[1], sizeof(int));
    BTreeNode *n2 = BTree_InsertRight(btree, &val[3], sizeof(int));
    BTree_InsertLeft(n1, &val[2], sizeof(int));
    BTree_PrintInt(btree);
}