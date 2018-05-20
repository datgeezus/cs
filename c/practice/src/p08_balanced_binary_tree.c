#include "btree/btree.h"

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
    size_t i = 0;
    BTreeNode *root, *left, *right;
    const int values[] = { 5, 8, 6, 1, 2, 3, 5 };

    root = BTree_NewNode(&values[0], sizeof(*values));
    left = BTree_InsertLeft(root, &values[1], sizeof(*values));
    right = BTree_InsertRight(root, &values[2], sizeof(*values));
    BTree_InsertLeft(left, &values[3], sizeof(*values));
    BTree_InsertRight(left, &values[4], sizeof(*values));
    BTree_InsertLeft(right, &values[5], sizeof(*values));
    BTree_InsertRight(right, &values[6], sizeof(*values));

    BTree_PrintPreorderInt(root);
}

static int btree__foreach(BTreeNode *node, const void *udata)
{

}