import sys


# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# <p>
# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

def max_profit(prices: list)-> int:
    buy, max_profit, old_profit = -sys.maxsize, 0, 0
    for ind, price in enumerate(prices):
        temp = max_profit
        buy = max(buy, old_profit - price)
        max_profit = max(max_profit, buy + price)
        old_profit = temp
    return max_profit

if __name__ == "__main__":
    res = max_profit([1, 2, 3, 0, 2])
    print(res)
    assert res == 3

