#include "btree.h"
#include "stack/stack.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct btreenode
{
    void *data;
    BTreeNode *left;
    BTreeNode *right;
};

static int btree__foreach_printint(const void *data, const void *userData);

BTreeNode *BTree_NewNode(const void *data, size_t dataSize)
{
    BTreeNode *This = calloc(1, sizeof(BTreeNode));
    This->data = calloc(1, dataSize);
    memcpy(This->data, data, dataSize);

    return This;
}

BTreeNode *BTree_InsertLeft(BTreeNode *root, const void *data, size_t dataSize)
{
    root->left = BTree_NewNode(data, dataSize);
    return root->left;
}

BTreeNode *BTree_InsertRight(BTreeNode *root, const void *data, size_t dataSize)
{
    root->right = BTree_NewNode(data, dataSize);
    return root->right;
}

void *BTree_GetData(BTreeNode *node)
{
    void *data = NULL;

    if (NULL != node)
    {
        data = node->data;
    }

    return data;
}

int BTree_GetDataInt(BTreeNode *node)
{
    int data = 0;
    void *ndata = BTree_GetData(node);

    if (NULL != ndata)
    {
        data = *(int *)ndata;
    }

    return data;
}

void BTree_PrintPreorderInt(BTreeNode *root)
{
    int ret = BTree_DFS_Preorder(root, btree__foreach_printint, NULL);
}

int BTree_DFS_Preorder(BTreeNode *root, BTreeForEach cb, const void *userData)
{
    int completed = 1;
    Stack *visit = Stack_New();

    Stack_PushPtr(visit, root);
    while (!Stack_IsEmpty(visit))
    {
        BTreeNode *node = (BTreeNode *)Stack_PopPtr(visit);
        int exit = cb(node->data, userData);
        if (1 == exit)
        {
            completed = 0;
            break;
        }
        else
        {
            if (NULL != node->right)
            {
                Stack_PushPtr(visit, node->right);
            }
            if (NULL != node->left)
            {
                Stack_PushPtr(visit, node->left);
            }
        }
    }

    return completed;
}

static int btree__foreach_printint(const void *data, const void *userData)
{
    printf("(%d) ", *(int *)data);
    return 0;
}
