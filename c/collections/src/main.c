#include "linkedlist/linkedlist.h"
#include "stack/stack.h"
#include <stdio.h>

static void test__linkedlist();
static void test__stack();

int main()
{
	test__linkedlist();
	test__stack();

	getchar();
}

static void test__linkedlist()
{
	printf("LinkedList text ...\n");

	LinkedList *list = LinkedList_New();
	LinkedList_AppendInt(list, 2);
	LinkedList_AppendInt(list, 4);
	LinkedList_AppendInt(list, 3);
	LinkedList_AppendInt(list, 9);

	LinkedList_PrintInt(list);
}

static void test__stack()
{
	printf("LinkedList text ...\n");

	Stack *stack = Stack_New();
	Stack_PushInt(stack, 1);
	Stack_PushInt(stack, 2);
	Stack_PushInt(stack, 3);
	Stack_PushInt(stack, 4);
	Stack_PushInt(stack, 5);
	Stack_PushInt(stack, 6);
	Stack_Pop(stack);
	Stack_Pop(stack);
	Stack_PushInt(stack, 7);

	Stack_PrintInt(stack);
}