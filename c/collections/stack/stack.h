#ifndef _STACK_H_

#include <stdlib.h>

typedef struct stack Stack;

Stack *Stack_New();
int Stack_IsEmpty(Stack *This);
void Stack_Push(Stack *This, void *data, size_t dataSize);
void Stack_Pop(Stack *This);
void *Stack_Peek(Stack *This);

void Stack_PushInt(Stack *This, int data);
int Stack_PopInt(Stack *This);
void Stack_PrintInt(Stack *This);

void Stack_PushChar(Stack *This, char data);
char Stack_PopChar(Stack *This);
void Stack_PrintChar(Stack *This);

#endif // !_STACK_H_
