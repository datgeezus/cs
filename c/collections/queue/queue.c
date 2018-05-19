#include "queue.h"
#include "stack/stack.h"
#include <stdlib.h>

struct queue
{
    Stack *in;
    Stack *out;
};

Queue *Queue_New()
{
    Queue *This = calloc(1, sizeof(struct queue));

    This->in = Stack_New();
    This->out = Stack_New();

    return This;
}

void *Queue_Peek(Queue *This)
{
    return Stack_Peek(This->out);
}

void Queue_Enqueue(Queue *This, void *data, size_t dataSize)
{
    Stack_Push(This->in, data, dataSize);
}

int Queue_IsEmpty(Queue *This)
{
    return Stack_IsEmpty(This->out) && Stack_IsEmpty(This->in);
}

void Queue_Deque(Queue *This)
{
}

void Queue_EnqueuePtr(Queue *This, void *data)
{
    Stack_PushPtr(This->in, data);
}

void *Queue_DequePtr(Queue *This)
{
    if (Stack_IsEmpty(This->out))
    {
        while (!Stack_IsEmpty(This->in))
        {
            void *newest = Stack_PopPtr(This->in);
            Stack_PushPtr(This->out, newest);
        }
    }

    return Stack_PopPtr(This->out);
}


void Queue_EnqueueInt(Queue *This, int data)
{
    Stack_Push(This->in, &data, sizeof(int));
}

int Queue_DequeInt(Queue *This)
{
    if (Stack_IsEmpty(This->out))
    {
        while (!Stack_IsEmpty(This->in))
        {
            int newest = Stack_PopInt(This->in);
            Stack_PushInt(This->out, newest);
        }
    }

    return Stack_PopInt(This->out);
}