# Arrays
## Two pointers
```python
def fun(arr: list[int]):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Logic depending on problem
        # Logic to update left and/or right
        left += 1
        right += 1
```
## Sliding window
```python
def fun(arr: list[int]):
    left l 0
    for right in arr:
        # logic to add element at arr[right]
        while left < right and constraint:
            # logic to remove element at arr[left]
            left += 1

        # logic to update answer
```

## Prefix sums
```python
prefix = [nums[0]]
for i in nums[1:]:
    prefix.append(nums[i] + prefix[end])
```

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

# Stacks and queues
## Stacks
## Queues
## Monotonic

```python
stack = []
for num in nums:
    while stack and stack[-1] >= num:
        stack.pop()
    # logic depending on the problem
    stack.push(num)
```

### Daily Temperatures
Given an array of integers `temperatures` that represents the daily temperatures,
return an array `ans` such that `ans[i]` is the number of days you have to wait after
the ith day to get a warmer temperature.
If there is no future day that is warmer, `ans[0] = 0`

```python
def daily_temps(temperatures: list[int]) -> list[int]:
    stack = []
    ans = [0 for _ in temperatures]

    for i in range(len(temperatures)):
        top = stack[-1]
        while stack and temperatures[top] < temperatures[i]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans
```
