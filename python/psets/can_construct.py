def can_construct(target:str, words:list[str], memo:dict=None):
    memo = {} if memo is None else memo
    if target == '': return True
    if target in memo: return memo[target]

    for word in words:
        ans = target.find(word)
        # pick only prefix
        if ans == 0:
            suffix = target[len(word):]
            if can_construct(suffix, words, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False

if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
    print(can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
        ["e", "ee", "eee", "eeee", "eeeee"])) # False