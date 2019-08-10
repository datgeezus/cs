#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include "hashtable/hashtable.h"
#include "trie.h"

typedef struct node TNode;

struct node {
    size_t size;
    char c;
    unsigned char isWord;
    HashTable *children;
};

struct trie {
    TNode *start;
};

struct tdata {
    void *udata;
    HashTableForEach cb;
};

static TNode *trie__node_new(const char c);
static void trie__for_each(const char *key, void *data, void* uData);
static void trie__for_each_print(const char c, void *data, void* uData);

Trie *Trie_New()
{
    Trie *This = calloc(1, sizeof(Trie));

    This->start =  calloc(1, sizeof(TNode));
    This->start->c = '*';
    This->start->size = 0;
    This->start->children = HashTable_New();

    return This;
}

void Trie_AddStr(Trie *This, const char *str)
{
    char i = 0;
    This->start->size = 1;
    TNode *curr = This->start;
    for(;  i < strlen(str); ++i)
    {
        char car[2] = { str[i], 0};
        TNode *new = HashTable_Find(curr->children, car);
        if(NULL == new)
        {
            new = trie__node_new(car);
            HashTable_InsertPtr(curr->children, car, new);
        }

        new->size += 1;
        curr = new;
    }
    curr->isWord = 1;
}

void Trie_Find(Trie *This, const char *str)
{

}

void Trie_Print(Trie *This)
{
   Trie_ForEach(This, trie__for_each_print, NULL);
}

void Trie_ForEach(Trie *This, TrieForEach cb, void *udata)
{
    TNode *curr = This->start;
    struct tdata data = { udata, cb  };
    HashTable_ForEach(This->start->children, trie__for_each, (void *)&data);
}

static TNode *trie__node_new(const char c)
{
    TNode *new = calloc(1, sizeof(TNode));
    new->c = c;
    new->size = 0;
    new->children = HashTable_New();
    return new;
}

static void trie__for_each(const char *key, void *data, void* uData)
{
    struct tdata *tdata = uData;
    TNode *node = data;
    tdata->cb(key[0], node, tdata->udata);
    HashTable_ForEach(node->children, trie__for_each, uData);
}

static void trie__for_each_print(const char c, void *data, void* uData)
{
    TNode *node = data;
    printf("%c", c);
    if(node->isWord)
    {
        printf("\n");
    }
}