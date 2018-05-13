#include "linkedlist.h"
#include <string.h>
#include <stdio.h>

typedef struct node Node;

struct node
{
	void *data;
	struct node *next;
};

struct linkedList
{
	Node *head;
};

static Node *linkedlist__new_node(void *data, size_t dataSize);

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
	Node *new = linkedlist__new_node(data, dataSize);
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

void LinkedList_AppendInt(LinkedList *This, int data)
{
	LinkedList_Append(This, &data, sizeof(int));
}

static Node *linkedlist__new_node(void *data, size_t dataSize)
{
	Node *This = calloc(1, sizeof(struct node));
	This->data = calloc(1, dataSize);
	memcpy(This->data, data, dataSize);
	return This;
}