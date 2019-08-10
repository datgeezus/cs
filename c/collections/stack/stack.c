#include "stack.h"
#include <stdio.h>
#include <string.h>

typedef struct node Node;

struct node
{
	void *data;
	struct node *next;
};

struct stack
{
	Node *top;
	size_t size;
};

static Node *stack__new_node(void *data, size_t dataSize);
static stack__free_node(Node **node);

Stack *Stack_New()
{
	Stack *This = calloc(1, sizeof(struct stack));
	return This;
}

size_t Stack_Size(Stack *This)
{
	return This->size;
}

int Stack_IsEmpty(Stack *This)
{
	return This->top == NULL;
}

void Stack_Push(Stack *This, void *data, size_t dataSize)
{
	Node *new = stack__new_node(data, dataSize);
	new->next = This->top;
	This->top = new;
	This->size += 1;
}

void Stack_PushPtr(Stack *This, const void *data)
{
    Node *new = calloc(1, sizeof(Node));
    new->data = data;
    new->next = This->top;
    This->top = new;
	This->size += 1;
}

void Stack_PushInt(Stack * This, int data)
{
	Stack_Push(This, &data, sizeof(int));
}

void Stack_Pop(Stack *This)
{
	Node *next = This->top->next;
	stack__free_node(&This->top);
	This->top = next;
	This->size -= 1;
}

void *Stack_PopPtr(Stack *This)
{
    void *data = Stack_Peek(This);
	Node *next = This->top->next;
    free(This->top);
	This->top = next;
	This->size -= 1;
    return data;
}

int Stack_PopInt(Stack * This)
{
	int data = *(int *)Stack_Peek(This);
	Stack_Pop(This);
	return data;
}

void *Stack_Peek(Stack *This)
{
	return This->top->data;
}

void Stack_PrintInt(Stack * This)
{
	Node *curr = This->top;
	while (NULL != curr)
	{
		printf("Node data (int): %d\n", *(int *)curr->data);
		curr = curr->next;
	}
}

void Stack_PushChar(Stack *This, char data)
{
    Stack_Push(This, &data, sizeof(char));
}

char Stack_PopChar(Stack *This)
{
    char data = *(char *)Stack_Peek(This);
	Stack_Pop(This);
	return data;
}

void Stack_PrintChar(Stack *This)
{

}

/****************************************************************************/
static Node *stack__new_node(void *data, size_t dataSize)
{
	Node *This = calloc(1, sizeof(struct node));
	This->data = calloc(1, dataSize);
	memcpy(This->data, data, dataSize);
	return This;
}

static stack__free_node(Node **node)
{
	void *data = (*(node))->data;
	free(data);
	free(*node);
}