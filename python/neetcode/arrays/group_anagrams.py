"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

from collections import defaultdict, Counter


def group_anagrams(strs: list[str]) -> list[list[str]]:
    def index_of(s: str):
        return ord(s) - ord("a")

    mem = defaultdict(list)

    for s in strs:
        count = [0] * 26  # a-z
        for c in s:
            count[index_of(c)] += 1
        mem[tuple(count)].append(s)
    return list(mem.values())


if __name__ == "__main__":
    exp = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert all(
        [
            sorted(ans) in sorted(exp)
            for ans in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        ]
    )
