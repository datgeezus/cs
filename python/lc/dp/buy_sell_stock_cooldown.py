"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve.
You may complete as many transactions as you like (i.e., buy one and sell one share of
the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the
stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0


## Solution

f(day, holding)

Decision:
- Buy: -prices[i] + f(i + 1, holding=True), if holding=False 
- Sell: prices[i] + f(i + 2, holding=False), if holding=True
- Skip: f(i+1, holding=holding)

f(i) = max(buy, sell, skip)

Base case: i >= len(prices)

"""

from functools import cache

def profit(prices: list[int]):
    n_prices = len(prices)

    @cache
    def f(i: int, holding: bool) -> int:
        if i >= n_prices:
            return 0

        ans = f(i+1, holding) # Skip
        if holding: # Sell
            ans = max(ans, prices[i] + f(i+2, False))
        else:       # Buy
            ans = max(ans, -prices[i] + f(i+1, True))

        return ans

    return f(0, False)


if __name__ == "__main__":
    prices = [1,2,3,0,2]
    ans = profit(prices)
    assert ans == 3, f"Expected=3, actual={ans}"
    print(ans)

    prices = [1]
    ans = profit(prices)
    assert ans == 0, f"Expected=0, actual={ans}"
    print(ans)
