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
	printf("**************\n");
}

static void test__stack()
{
	printf("Stack test ...\n");

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
	printf("Set test ...\n");
    HashSet *set = HashSet_New();
    HashSet_Insert(set, "Hello");
    HashSet_Insert(set, "Hi");
    HashSet_Insert(set, "Hallo");
    HashSet_Insert(set, "Hola");
    HashSet_Print(set);
	printf("**************\n");
}