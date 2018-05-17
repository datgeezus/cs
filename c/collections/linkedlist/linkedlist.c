#include "linkedlist.h"
#include <string.h>
#include <stdio.h>

typedef struct node Node;

enum dataType
{
    LIST_INT,
    LIST_STR,
    LIST_FLT,
    LIST_CST,
};

struct callback
{
    ForEach fe;
    enum dataType type;
};

struct node
{
	void *data;
    enum dataType type;
	struct node *next;
};

struct linkedList
{
	Node *head;
};

static Node *linkedlist__new_node(void *data, size_t dataSize, enum dataType type);
static void linkedlist__foreach_print(const void *data, const void *type);
static void linkedlist__append(LinkedList *This, void *data, size_t dataSize, enum dataType type);

LinkedList *LinkedList_New()
{
	LinkedList *This = calloc(1, sizeof(struct linkedList));

	return This;
}

void LinkedList_PrintInt(LinkedList * This)
{
	Node *curr = This->head;
    while (curr)
    {
        printf("Node data (int): %d\n", *(int *)curr->data);
        curr = curr->next;
    }
}

void LinkedList_Append(LinkedList *This, void *data, size_t dataSize)
{
    linkedlist__append(This, data, dataSize, LIST_CST);
}

void LinkedList_AppendInt(LinkedList *This, int data)
{
    linkedlist__append(This, &data, sizeof(int), LIST_INT);
}

void LinkedList_ForEach(LinkedList *This, ForEach cb, const void *userData)
{
    if (NULL != This && NULL != cb)
    {
        Node *curr = This->head;
        while (NULL != curr)
        {
            cb(curr->data, userData);
            curr = curr->next;
        }
    }
}

static void linkedlist__append(LinkedList *This, void *data, size_t dataSize, enum dataType type)
{
	Node *new = linkedlist__new_node(data, dataSize, type);
	if (NULL != This->head)
	{
		Node *curr = This->head;
		while (NULL != curr->next)
		{
			curr = curr->next;
		}
		curr->next = new;
	}
	else
	{
		This->head = new;
	}
}

static Node *linkedlist__new_node(void *data, size_t dataSize, enum dataType type)
{
	Node *This = calloc(1, sizeof(struct node));
    This->type = type;
	This->data = calloc(1, dataSize);
	memcpy(This->data, data, dataSize);
	return This;
}

static void linkedlist__foreach_print(const void *data, const void *type)
{
    enum dataType dtype = *(enum dataType *)type;
    switch (dtype)
    {
    case LIST_INT:
    {
        int d = *(int *)data;
        printf("[%d] ", d);
        break;
    }
    case LIST_STR:
    {
        char *d = (char *)data;
        printf("[%s] ", d);
        break;
    }
    default:
        break;
    }
}
