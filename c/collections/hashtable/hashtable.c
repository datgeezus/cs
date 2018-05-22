#include "hashtable.h"
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define TABLE_SIZE  1024
#define TABLE_SEED  4815
#define TOLOWER     (char)0x20 

typedef struct node Node;

struct node
{
    char *key;
    void *data;
    size_t size;
    Node *next;
};

struct hashtable
{
    size_t size;
    size_t n;
    Node *table[TABLE_SIZE];
    uint32_t hashes[TABLE_SIZE];
};

static Node *hashtable__node_new(const char *key, void *data, size_t size);
static Node *hashtable__node_find(Node *root, const char *key);
static Node *hashtable__find(HashTable *This, const char *key);
static void hashtable__foreach_print(const char *key, void *data, void *udata);
static uint32_t hash_function(const char *key);

HashTable *HashTable_New()
{
    HashTable *This = calloc(1, sizeof(HashTable));

    return This;
}

void HashTable_Insert(HashTable *This, const char *key, void *data, size_t size)
{
    uint32_t hash = hash_function(key);
    if (NULL == This->table[hash])
    {
        /* hash not found, create new node */
        Node *n = hashtable__node_new(key, data, size);
        This->table[hash] = n;
        This->size += 1;
        This->hashes[This->n] = hash;
        This->n += 1;
    }
    else
    {
        /* hash found, search for existing node by key */
        Node *n = hashtable__node_find(This->table[hash], key);
        if (NULL == n)
        {
            /* node not found, create a new one */
            n = hashtable__node_new(key, data, size);
            n->next = This->table[hash];
            This->table[hash] = n;
            This->size += 1;
        }
    }
}

int HashTable_In(HashTable *This, const char *key)
{
    return NULL != hashtable__find(This, key);
}

void *HashTable_Find(HashTable *This, const char *key)
{
    void *data = NULL;
    Node *node = hashtable__find(This, key);

    if (NULL != node)
    {
        data = node->data;
    }

    return data;
}

static Node *hashtable__find(HashTable *This, const char *key)
{
    Node *node = NULL;

    if (NULL != This)
    {
        uint32_t hash = hash_function(key);
        if (NULL != This->table[hash])
        {
            node = hashtable__node_find(This->table[hash], key);
        }
    }

    return node;
}

void HashTable_ForEach(HashTable *This, HashTableForEach cb, void *uData)
{
    if (NULL != This && NULL != cb)
    {
        int i = 0;
        for (; i < This->n; ++i)
        {
            Node *n = NULL;
            for(n = This->table[This->hashes[i]]; NULL != n; n = n->next)
            {
                cb(n->key, n->data, uData);
            }
        }
    }
}

void HashTable_Print(HashTable *This)
{
    HashTable_ForEach(This, hashtable__foreach_print, NULL);
    printf("\n");
}

void HashTable_InsertPtr(HashTable *This, const char *key, void *data)
{
    HashTable_Insert(This, key, data, 0);
}

/* private ******************************************************************/
static Node *hashtable__node_new(const char *key, void *data, size_t size)
{
    Node *node = calloc(1, sizeof(Node));
    node->key = calloc(1, strlen(key) + 1);
    strcpy(node->key, key);
    node->size = size;
    if (size > 0)
    {
        node->data = calloc(1, size);
        memcpy(node->data, data, size);
    }
    else
    {
        node->data = data;
    }
    return node;
}

static Node *hashtable__node_find(Node *root, const char *key)
{
    Node *n = NULL;

    if (NULL != root)
    {
        Node *curr = NULL;
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

static void hashtable__foreach_print(const char *key, void *data, void *udata)
{
    printf("[%s] ", key);
}
