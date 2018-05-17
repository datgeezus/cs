#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_

#include <stdlib.h>

typedef struct linkedList LinkedList;
typedef void (*ForEach)(const void *data, const void *userData);

LinkedList *LinkedList_New();
void LinkedList_ForEach(LinkedList *This, ForEach cb, const void *userData);
void LinkedList_PrintInt(LinkedList *This);
void LinkedList_Append(LinkedList *This, void *data, size_t dataSize);
void LinkedList_AppendInt(LinkedList *This, int data);

#endif // !_LINKEDLIST_H_
