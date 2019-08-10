#ifndef _HEAP_H_

#include <stdio.h>

typedef struct heap Heap;

typedef int(*HeapDataCompare)(void *data1, void* data2, void *uData);

Heap *Heap_New(HeapDataCompare cb);
void Heap_Add(Heap *This, void *data);
void *Heap_Peek(Heap *This);
void *Heap_Pop(Heap *This);

#endif // !_HEAP_H_
