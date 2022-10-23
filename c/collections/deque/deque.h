#ifndef _DEQUE_H_
#define _DEQUE_H_

#include "result/result.h"


typedef struct deque Deque;
typedef struct dequeResult DequeResult;

Deque *Deque_New();
void Deque_Append(Deque *deque, void* value);
Result Deque_PopLeft(Deque *deque);
Result Deque_Pop(Deque *deque);
int Deque_IsEmpty(Deque *deque);


#endif