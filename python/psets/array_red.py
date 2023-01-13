import heapq

def reduce(nums: list[int]) -> int:
    heapq.heapify(nums)
    ans = 0
    while len(nums) >= 2:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        cost = a + b
        ans += cost
        heapq.heappush(nums, cost)

    return ans


if __name__ == "__main__":
    cost = reduce([4,4,4,4,6])
    print(cost)

    cost = reduce([4,6,8])
    print(cost)
