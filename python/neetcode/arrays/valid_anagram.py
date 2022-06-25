# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_mem = {}
    t_mem = {}
    for i, _ in enumerate(s):
        s_mem[s[i]] = 1 + s_mem.get(s[i], 0)
        t_mem[t[i]] = 1 + t_mem.get(t[i], 0)

    for char, s_count in s_mem.items():
        if s_count != t_mem.get(char, 0):
            return False
    return True


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram")
    assert is_anagram("rat", "cat") is False
