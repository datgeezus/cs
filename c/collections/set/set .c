#include "set.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define TABLE_SIZE  1024
#define TABLE_SEED  4815
#define TOLOWER     (char)0x20 

typedef struct node Node;

struct node
{
    char *key;
    Node *next;
};

struct set
{
    int size;
    Node *table[TABLE_SIZE];
    uint32_t hashes[TABLE_SIZE];
};

static Node *set__node_new(const char *key);
static Node *set__node_find(Node *root, const char *key);
static void set__foreach_print(const char *key);
static uint32_t hash_function(const char *key);


Set *Set_New()
{
    Set *This = calloc(1, sizeof(struct set));
    This->size = 0;
    memset(This->table, NULL, TABLE_SIZE);
    memset(This->hashes, 0U, TABLE_SIZE);

    return This;
}

size_t Set_GetSize(Set *This)
{
    return This->size;
}

void Set_Insert(Set *This, const char *key)
{
    uint32_t hash = hash_function(key);
    Node *n = set__node_new(key);
    if (NULL == This->table[hash])
    {
        This->table[hash] = n;
        This->hashes[This->size] = hash;
        This->size += 1;
    }
    else
    {
        Node *found = set__node_find(This->table[hash], key);
        if (NULL == found)
        {
            n->next = This->table[hash];
            This->table[hash] = n;
            This->hashes[This->size] = hash;
            This->size += 1;
        }
    }
}

int Set_In(Set *This, const char *key)
{
    uint32_t hash = hash_function(key);
    Node *f = set__node_find(This->table[hash], key);
    return NULL != f;
}

void Set_ForEachStr(Set *This, ForEachStr cb)
{
    if (NULL != This && NULL != cb)
    {
        int i = 0;
        for (i = 0; i < This->size; ++i)
        {
            Node *curr = This->table[This->hashes[i]];
            while (NULL != curr)
            {
                cb(curr->key);
                curr = curr->next;
            }
        }
    }
}

void Set_PrintChar(Set *This)
{
    Set_ForEachStr(This, set__foreach_print);
    printf("\n");
}

void Set_InsertChar(Set *This, char data);
int Set_CharIn(Set *This, char data);
void Set_EraseChar(Set *This, char data);

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

static Node *set__node_new(const char *key)
{
    Node *node = calloc(1, sizeof(Node));
    node->key = calloc(strlen(key), sizeof(char));
    strcpy(node->key, key);
    return node;
}

static Node *set__node_find(Node *root, const char *key)
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

static void set__foreach_print(const char *key)
{
    printf("[%s] ", key);
}
