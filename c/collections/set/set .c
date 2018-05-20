#include "set.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define TABLE_SIZE  1024
#define TABLE_SEED  4815
#define TOLOWER     (char)0x20 

typedef struct hashsetnode HSNode;

struct hashsetnode
{
    char *key;
    HSNode *next;
};

struct hashset
{
    size_t size;
    size_t n;
    HSNode *table[TABLE_SIZE];
    uint32_t hashes[TABLE_SIZE];
};

static HSNode *hashset__node_new(const char *key);
static HSNode *hashset__node_find(HSNode *root, const char *key);
static void hashset__foreach_print(const char *key, void *udata);
static uint32_t hash_function(const char *key);


HashSet *HashSet_New()
{
    HashSet *This = calloc(1, sizeof(HashSet));
    This->size = 0;
    memset(This->table, 0U, TABLE_SIZE);
    memset(This->hashes, 0U, TABLE_SIZE);

    return This;
}

size_t HashSet_GetSize(HashSet *This)
{
    return This->size;
}

void HashSet_Insert(HashSet *This, const char *key)
{
    uint32_t hash = hash_function(key);
    if (NULL == This->table[hash])
    {
        /* hash not found, create new node */
        HSNode *n = hashset__node_new(key);
        This->table[hash] = n;
        This->hashes[This->size] = hash;
        This->n += 1;
        This->size += 1;
    }
    else
    {
        /* hash found, search for existing node by key */
        HSNode *n = hashset__node_find(This->table[hash], key);
        if (NULL == n)
        {
            /* node not found, create a new one */
            n = hashset__node_new(key);
            n->next = This->table[hash];
            This->table[hash] = n;
            This->hashes[This->size] = hash;
            This->size += 1;
        }
    }
}

int HashSet_In(HashSet *This, const char *key)
{
    uint32_t hash = hash_function(key);
    HSNode *f = hashset__node_find(This->table[hash], key);
    return NULL != f;
}

void HashSet_ForEach(HashSet *This, HashSetForEach cb, void *udata)
{
    if (NULL != This && NULL != cb)
    {
        int i = 0;
        for (; i < This->n; ++i)
        {
            HSNode *n = NULL;
            for(n = This->table[This->hashes[i]]; NULL != n; n = n->next)
            {
                cb(n->key, udata);
            }
        }
    }
}

void HashSet_Print(HashSet *This)
{
    HashSet_ForEach(This, hashset__foreach_print, NULL);
}

/****************************************************************************/
static uint32_t hash_function(const char *key)
{
    char    c;
    unsigned int h;

    h = TABLE_SEED;
    for (; (c = *key) != '\0'; key++)
    {
        h ^= ((h << 5) + (c | TOLOWER) + (h >> 2));
    }
    return((unsigned int)((h & 0x7fffffff) % TABLE_SIZE));
}

static HSNode *hashset__node_new(const char *key)
{
    HSNode *node = calloc(1, sizeof(HSNode));
    node->key = calloc(strlen(key), sizeof(char));
    strcpy(node->key, key);
    return node;
}

static HSNode *hashset__node_find(HSNode *root, const char *key)
{
    HSNode *n = NULL;

    if (NULL != root)
    {
        HSNode *curr = NULL;
        for (curr = root; NULL != curr; curr = curr->next)
        {
            if (0 == strcmp(curr->key, key))
            {
                n = curr;
                break;
            }
        }
    }

    return n;
}

static void hashset__foreach_print(const char *key, void *udata)
{
    printf("[%s] ", key);
}
