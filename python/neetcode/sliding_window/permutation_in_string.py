"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""
from collections import Counter

def ascii_to_int(at: str) -> int:
    return ord(at) - ord('a')

def permutations(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    # Build a map using an array, index is the key
    s1_count = [0] * 26
    s2_count = [0] * 26
    for i,_ in enumerate(s1):
        s1_count[ascii_to_int(s1[i])] += 1
        s2_count[ascii_to_int(s2[i])] += 1

    print(f"s1_c:{Counter(s1)}, s2_c:{Counter(s2)}")

    matches = 0
    for i in range(26):
        matches += 1 if s1_count[i] == s2_count[i] else 0

    l = 0
    s1_len = len(s1)
    for r in range(len(s1), len(s2)):
        print(f"l:{l}, r:{r}, s2[l]:{s2[l]}, s2[r]:{s2[r]}")
        index = ascii_to_int(s2[r])
        s2_count[index] += 1
        if s1_count[index] == s2_count[index]:
            matches += 1
        elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1

        # matches += 1 if s1_count[index] == s2_count[index] else - 1

        index = ascii_to_int(s2[l])
        # matches += 1 if s1_count[index] == s2_count[index] else - 1
        s2_count[index] -= 1
        if s1_count[index] == s2_count[index]:
            matches += 1
        elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1
        l += 1

    return matches == 26


if __name__ == "__main__":
    assert permutations("ab", "eidbaooo") == True
    assert permutations("ab", "eidboaoo") == False
