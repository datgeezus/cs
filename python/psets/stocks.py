"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
"""
from typing import List

def max_profit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i]-min_price)

    return max_profit

if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4])) # Expected: 5
    print(max_profit([7,6,4,3,1])) # Expected: 0
    print(max_profit([1,2,4])) # Expected: 3