#ifndef _HASHTABLE_H_
#define _HASHTABLE_H_

#include <stdlib.h>

typedef struct hashtable HashTable;
typedef void(*HashTableForEach)(const char *key, void *data, void* uData);

HashTable *HashTable_New();
void HashTable_Insert(HashTable *This, const char *key, void *data, size_t size);
void HashTable_ForEach(HashTable *This, HashTableForEach cb, void *uData);
void HashTable_Print(HashTable *This);
void *HashTable_Find(HashTable *This, const char *key);

void HashTable_InsertPtr(HashTable *This, const char *key, void *data);

#endif // !_HASHTABLE_H_
