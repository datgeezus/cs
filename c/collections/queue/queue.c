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

void Queue_Deque(Queue *This)
{
}


void Queue_EnqueueInt(Queue *This, int data)
{
    Stack_Push(This->in, &data, sizeof(int));
}

int Queue_DequeInt(Queue *This)
{
    int max = 0;

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

void Queue_PrintInt(Queue *This, int data)
{
}
