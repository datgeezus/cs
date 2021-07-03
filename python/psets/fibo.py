"""
Find the nth number in the Fibonacci sequence
     n: 0, 1, 2, 3, 4, 5, 6,  7,  8
fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

# Recursive and memoized
#  time: O(n)
# space: O(n)
def fib(n, memo={}):
    # base cases
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    if n in memo: return memo[n]

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


# Tabulation
def fib_tab(n):
    pass

if __name__ == "__main__":
    print(fib(0))
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))