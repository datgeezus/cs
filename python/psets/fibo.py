"""
Find the nth number in the Fibonacci sequence
     n: 0, 1, 2, 3, 4, 5, 6,  7,  8
fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

# Recursive and memoized
#  time: O(n)
# space: O(n)
def fib(n, memo=None):
    memo = {} if memo is None else memo
    # base cases
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# Tabulation
#  time: O(n)
# space: O(n)
def fib_tab(n):
    # base cases
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    table = (n + 1) * [0]
    table[1] = 1
    table[2] = 1
    for i in range(3, n + 1):
        table[i] = table[i - 2] + table[i - 1]
    return table[n]


if __name__ == "__main__":
    print(fib(0))
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
    print(fib_tab(0))
    print(fib_tab(6))
    print(fib_tab(7))
    print(fib_tab(8))
    print(fib_tab(50))
