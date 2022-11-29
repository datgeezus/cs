import heapq
from collections import defaultdict

def reorder(words: list[str]) -> list[str]:

    frequencies = defaultdict(int)
    for word in words:
        frequencies[word] += 1

    heap = []
    for word,freq in frequencies.items():
        # use negative values to simulate a max-heap
        heapq.heappush(heap, (-1*freq, word))

    ans = []
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        ans.append(first[1])
        ans.append(second[1])
        if first[0] < 0:
            heapq.heappush(heap, (first[0]+1, first[1]))
        if second[0] < 0:
            heapq.heappush(heap, (second[0]+1, second[1]))

    return ans


if __name__ == "__main__":
    ans = reorder(['a','a','a', 'b', 'b'])
    print(f"ans={ans}")

    ans = reorder(['a','a','a', 'b', 'b', 'c'])
    print(f"ans={ans}")

    ans = reorder(['a','a', 'b', 'b', 'c', 'c'])
    print(f"ans={ans}")
