# Arrays
## Sliding window
## Prefix sums

# Hashing
## Counting

```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = 0
    curr = 0

    for num in nums:
        curr += num # constraint
        ans += counts[curr - k]
        counts[curr] += 1

    return ans
```

