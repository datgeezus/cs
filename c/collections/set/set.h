#ifndef _SET_H_

#include <stdio.h>

typedef struct set Set;
typedef void (*ForEachStr)(const char *key);

Set *Set_New();
size_t Set_GetSize(Set *This);
void Set_Insert(Set *This, const char *key);
int Set_In(Set *This, const char *key);
void Set_ForEachStr(Set *This, ForEachStr cb);
void Set_PrintChar(Set *This);

void Set_InsertChar(Set *This, char data);
int Set_CharIn(Set *This, char data);
void Set_EraseChar(Set *This, char data);

#endif // !_SET_H_
