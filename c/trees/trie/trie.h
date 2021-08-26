#ifndef _TRIE_H_
#define _TRIE_H_

typedef struct trie Trie;

typedef void(*TrieForEach)(const char c, void *data, void *udata);

Trie *Trie_New();
void Trie_AddStr(Trie *This, const char *str);
void Trie_Find(Trie *This, const char *str);
void Trie_Print(Trie *This);
void Trie_ForEach(Trie *This, TrieForEach cb, void *udata);

#endif // !_TRIE_H
