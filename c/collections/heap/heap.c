#include <stdlib.h>
#include "heap.h"

#define STARTING_CAPACITY (64)

struct heap
{
    int capacity;
    size_t size;
    void **items;
    HeapDataCompare cb;
    void *uData;
};

static int heap__get_left_child_idx(int parentIdx);
static int heap__get_right_child_idx(int parentIdx);
static int heap__get_parent_idx(int childIdx);
static int heap__has_left_child(Heap *This, int idx);
static int heap__has_right_child(Heap *This, int idx);
static int heap__has_parent(Heap *This, int idx);
static void *heap__get_left_child(Heap *This, int idx);
static void *heap__get_right_child(Heap *This, int idx);
static void *heap__get_parent(Heap *This, int idx);
static void heap__swap_node(Heap *This, int idx1, int idx2);
static void heap__check_capacity(Heap *This);
static void heap__heapify_down(Heap *This);
static void heap__heapify_up(Heap *This);

Heap *Heap_New(HeapDataCompare cb)
{
    Heap *This = calloc(1, sizeof(Heap));
    This->items = calloc(STARTING_CAPACITY, sizeof(void *));
    This->capacity = STARTING_CAPACITY;
    This->cb = cb;

    return This;
}

void Heap_Add(Heap *This, void *data)
{
    heap__check_capacity(This);
    This->items[This->size] = data;
    This->size += 1;
    heap__heapify_up(This);
}

void *Heap_Peek(Heap *This)
{
    void *ret = NULL;

    if(This->size > 0)
    {
        ret = This->items[0];
    }

    return ret;
}

void *Heap_Pop(Heap *This)
{
    void *ret = NULL;

    if(This->size > 0)
    {
        ret = This->items[0];
        This->size -= 1;
        This->items[0] = This->items[This->size];
        heap__heapify_down(This);
    }

    return ret;
}

static void heap__swap_node(Heap *This, int idx1, int idx2)
{
    void *tmp = This->items[idx1];
    This->items[idx1] = This->items[idx2];
    This->items[idx2] = tmp;
}

static void heap__check_capacity(Heap *This)
{
    if(This->size == This->capacity)
    {
        This->capacity *= 2;
        This->items = realloc(This->items, This->capacity * sizeof(void *));
    }
}

static void heap__heapify_down(Heap *This)
{
    int idx = 0;
    while (heap__has_left_child(This, idx))
    {
        int curr = heap__get_left_child_idx(idx);

        if(heap__has_right_child(This, idx) && This->cb(heap__get_right_child(This, idx), heap__get_left_child(This, idx), This->uData))
        {
            curr = heap__get_right_child_idx(idx);
        }

        if(This->cb(This->items[idx], This->items[curr], This->uData))
        {
            break;
        }
        else
        {
            heap__swap_node(This, idx, curr);
        }

        idx = curr;
    }
}

static void heap__heapify_up(Heap *This)
{
    int idx = This->size - 1;
    while(heap__has_parent(This, idx) && This->cb(heap__get_parent(This, idx), This->items[idx], This->uData))
    {
        heap__swap_node(This, heap__get_parent_idx(idx), idx);
        idx = heap__get_parent_idx(idx);
    }
}

static int heap__get_left_child_idx(int parentIdx)
{
    return (2 * parentIdx) + 1;
}

static int heap__get_right_child_idx(int parentIdx)
{
    return (2 * parentIdx) + 2;
}

static int heap__get_parent_idx(int childIdx)
{
    return (childIdx -1) / 2;
}

static int heap__has_left_child(Heap *This, int idx)
{
    return heap__get_left_child_idx(idx) < This->size;
}

static int heap__has_right_child(Heap *This, int idx)
{
    return heap__get_right_child_idx(idx) < This->size;
}

static int heap__has_parent(Heap *This, int idx)
{
    return heap__get_parent_idx(idx) >= 0;
}

static void *heap__get_left_child(Heap *This, int idx)
{
    int cIdx = heap__get_left_child_idx(idx);
    return This->items[cIdx];
}

static void *heap__get_right_child(Heap *This, int idx)
{
    int cIdx = heap__get_right_child_idx(idx);
    return This->items[cIdx];
}

static void *heap__get_parent(Heap *This, int idx)
{
    int pIdx = heap__get_parent_idx(idx);
    return This->items[pIdx];
}
