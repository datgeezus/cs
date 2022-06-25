"""
# Problem
Given a string s, find the length of the longest substring without repeating characters.

# Solution
Sliding window, keeping track of chars
"""


def longest_substring_lenght(s: str) -> int:
    if not s:
        return 0
    n = len(s)
    if n == 1:
        return 1
    used = set()
    longest = 0
    left = 0
    right = 0

    while right < n:
        if s[right] not in used:
            used.add(s[right])
            longest = max(longest, len(used))
            right += 1
        else:
            used.remove(s[left])
            left += 1
    return longest


if __name__ == "__main__":
    assert longest_substring_lenght("abcabcbb") == 3
    assert longest_substring_lenght("bbbbb") == 1
    assert longest_substring_lenght("pwwkew") == 3
    assert longest_substring_lenght("aab") == 2
    assert longest_substring_lenght("dvdf") == 3
