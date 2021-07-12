def all_construct(target, words):
    if target == '': return [[]]

    ans = []

    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, words)
            target_ways = [[word] + way for way in suffix_ways]
            ans += target_ways

    return ans

if __name__ == "__main__":
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))