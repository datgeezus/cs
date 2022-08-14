"""
# Problem
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.


# Solution
## Max heap

## Bucket sort


- count ocurrances of each element

- build an array where the index represents a frequency and the value is a list of the elements
  with such frequency
  
- traverse the freq array from last to first to get the k elems


input = [1,1,1,1,2,2,3]

count = {
    1:4, 
    2:2, 
    3:1
    }

freq = [[], [3], [2], [], [1]]
        0    1    2    3   4

"""

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # count the frequency of numbers
    count = Counter(nums)

    # List of frequency buckets, index represent frequency, buckets is the list of values
    freq = [[] for _ in range(len(nums) + 1)]
    for n, c in count.items():
        freq[c].append(n)

    ans = [
        n 
        for i in range(len(freq) - 1, 0, -1)
        for n in freq[i]
    ]

    return ans[:k] if len(ans) >= k else []


if __name__ == "__main__":
    assert top_k_frequent([1, 1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1, 1, 2, 2, 3], 1) == [1]
    assert top_k_frequent([1], 1) == [1]
