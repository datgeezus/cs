#ifndef _DEQUE_H_
#define _DEQUE_H_

enum DequeResultType
{
    OK,
    ERR
};

struct dequeResult
{
    enum DequeResultType type;
    void *value;
};

typedef struct deque Deque;
typedef struct dequeResult DequeResult;

Deque *Deque_New();
void Deque_Append(Deque *deque, void* value);
DequeResult Deque_PopLeft(Deque *deque);
DequeResult Deque_Pop(Deque *deque);
int Deque_IsEmpty(Deque *deque);


#endif