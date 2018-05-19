#ifndef _QUEUE_H_

#include <stdio.h>

typedef struct queue Queue;

Queue *Queue_New();

void *Queue_Peek(Queue *This);
void Queue_Enqueue(Queue *This, void *data, size_t dataSize);
void Queue_Deque(Queue *This);
int Queue_IsEmpty(Queue *This);

void Queue_EnqueueInt(Queue *This, int data);
int Queue_DequeInt(Queue *This);

void Queue_EnqueuePtr(Queue *This, void *data);
void *Queue_DequePtr(Queue *This);

#endif // !_QUEUE_H_
