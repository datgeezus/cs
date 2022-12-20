"""
You are given an array prices where prices[i] is the price of a given stock on the ith day,
and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6


## Solution



Decisions:
- Buy: -prices[i] + f(i+1, holding=True), if holding=False
- Sell: +prices[i] - fee + f(i+1, holding=False), if holding=True
- Skip: f(i+1, holding)

f(i) = max(buy, sell, skip)

Base case: i > len(prices)

"""
from functools import cache

def profit(prices: list[int], fee: int) -> int:
    n_prices = len(prices)

    @cache
    def f(i: int, holding: bool) -> int:
        if i >= n_prices:
            return 0

        ans = f(i+1, holding) # Skip
        if holding: # Sell
            ans = max(ans, prices[i] + f(i+1, False))
        else:       # Buy
            ans = max(ans, -prices[i] + f(i+1, True) - fee)

        return ans

    return f(0, False)


if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    fee = 2
    ans = profit(prices, fee)
    assert ans == 8, f"Expected=8, actual={ans}"
    print(ans)

    prices = [1,3,7,5,10,3]
    fee = 3
    ans = profit(prices, fee)
    assert ans == 6, f"Expected=6, actual={ans}"
    print(ans)
