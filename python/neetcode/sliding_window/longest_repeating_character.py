"""
You are given a string s and an integer k. You can choose any character of the string and change it
to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.
"""

from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    count = defaultdict(int)
    ans = 0
    left = 0

    for right, val in enumerate(s):
        count[val] += 1
        max_freq = max(count.values())
        while (window_lenght(left, right) - max_freq) > k:
            count[s[left]] -= 1
            left += 1
        ans = max(ans, window_lenght(left, right))

    return ans

def window_lenght(l: int, r: int) -> int:
    return (r - l) + 1


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
