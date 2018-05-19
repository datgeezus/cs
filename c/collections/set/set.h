#ifndef _SET_H_

#include <stdio.h>

typedef struct hashset HashSet;
typedef void (*HashSetForEach)(const char *key, void *udata);

HashSet *HashSet_New();
size_t HashSet_GetSize(HashSet *This);
void HashSet_Insert(HashSet *This, const char *key);
int HashSet_In(HashSet *This, const char *key);
void HashSet_ForEach(HashSet *This, HashSetForEach cb, void *udata);
void HashSet_Print(HashSet *This);


#endif // !_SET_H_
