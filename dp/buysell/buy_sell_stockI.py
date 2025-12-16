# #####  Buy and Sell only once   #####
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# <p>
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
# <p>
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# <p>
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
import sys


def max_profit(prices: list)-> int:
    max_profit, min_price = 0, prices[0]
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit

if __name__== "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    res = max_profit(prices)
    print(res)
    assert res == 5