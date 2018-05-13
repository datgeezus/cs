#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_

#include <stdlib.h>

typedef struct linkedList LinkedList;

LinkedList *LinkedList_New();
void LinkedList_PrintInt(LinkedList *This);
void LinkedList_Append(LinkedList *This, void *data, size_t dataSize);
void LinkedList_AppendInt(LinkedList *This, int data);

#endif // !_LINKEDLIST_H_
