# ######    Buy and sell at most k times    ######
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times
# and sell at most k times.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# <p>
# Example 1:
# <p>
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# <p>
# Example 2:
# <p>
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
import sys


def max_profit(prices: list, k: int) -> int:
    dp = [[-sys.maxsize, 0] for i in range(k + 1)]
    for ind, price in enumerate(prices):
        for j in range(1, k+1):
            dp[j][0] = max(dp[j][0], dp[j-1][1] - price)
            dp[j][1] = max(dp[j][1], dp[j][0] + price)
        # for j in range(k, 0, -1):
        #     dp[j][0] = max(dp[j][0], dp[j-1][1] - price)
        #     dp[j][1] = max(dp[j][1], dp[j][0] + price)
    return dp[k][1]

if __name__=="__main__":
    res = max_profit([3, 3, 5, 0, 0, 3, 1, 4], 2)
    print(res)
    assert res == 6