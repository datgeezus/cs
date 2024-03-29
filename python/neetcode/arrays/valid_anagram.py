"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_mem = Counter(s)
    t_mem = Counter(t)

    return s_mem == t_mem


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram")
    assert is_anagram("rat", "cat") is False
