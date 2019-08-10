#include "linkedlist/linkedlist.h"
#include "stack/stack.h"
#include "set/set.h"
#include "heap/heap.h"
#include <stdio.h>

static void test__linkedlist();
static void test__stack();
static void test__set();
static void test__heap();
static int test__heap_comparator_min(void *a, void *b, void *udata);

int main()
{
	test__linkedlist();
	test__stack();
    test__set();
	test__heap();

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

static void test__heap()
{
	int data[] = { 11, 4, 7, 3,  8, 9, 4, 9, 2, 30};
	int i = 0;
	printf("Heap test ...\n");
	Heap *minHeap = Heap_New(test__heap_comparator_min);
	for(; i < 10; ++i)
	{
		Heap_Add(minHeap, &data[i]);
	}
	int * min = (int *)Heap_Peek(minHeap);
	printf("Min value is %d", *min);
}

static int test__heap_comparator_min(void *a, void *b, void *udata)
{
	return *(int *)a > *(int *)b;
}