#include "linkedlist/linkedlist.h"
#include "stack/stack.h"
#include "set/set.h"
#include <stdio.h>

static void test__linkedlist();
static void test__stack();
static void test__set();

int main()
{
	test__linkedlist();
	test__stack();
    test__set();

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
	printf("Stack text ...\n");

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
	printf("**************\n");
}

static void test__set()
{
	printf("Set text ...\n");
    Set *set = Set_New();
    Set_Insert(set, "Hello");
    Set_Insert(set, "Hi");
    Set_Insert(set, "Hallo");
    Set_Insert(set, "Hola");
    Set_PrintChar(set);
	printf("**************\n");
}