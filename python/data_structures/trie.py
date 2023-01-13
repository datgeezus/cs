def build_trie(words: list[str]):
    WORD_KEY = "$"

    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # retrieve the next node; If not fofund, create empty
            node = node.setdefault(letter, {})
        # mark existance of a word in trie node
        node[WORD_KEY] = word

    return trie


if __name__ == "__main__":
    words = ["oath","pea","eat","rain"]
    trie = build_trie(words)
    print(trie)


    d = {
        'o': {
            'a': {
                't': {
                    'h': {
                        '$': 'oath'
                    }
                }
            }
        }, 
        'p': {
            'e': {
                'a': {
                    '$': 'pea'
                }
            }
        }, 
        'e': {
            'a': {
                't': {
                    '$': 'eat'
                }
            }
        }, 
        'r': {
            'a': {
                'i': {
                    'n': {
                        '$': 'rain'
                    }
                }
            }
        }
    }
