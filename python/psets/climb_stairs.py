"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def climb(n_steps: int, memo: dict=None) -> int:
    memo = {} if memo is None else memo
    if n_steps == 0: return 1
    if n_steps < 0: return 0
    if n_steps in memo: return memo[n_steps]
    ans = climb(n_steps-1, memo) + climb(n_steps-2, memo)
    memo[n_steps] = ans
    return ans


if __name__ == "__main__":
    print(climb(2))
    print(climb(3))
    print(climb(38))