import sys


## Buy once, sell once
def maxProfit(prices: list) -> int:
    min_price, max_profit = prices[0], 0
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit


def max_profitII(prices: list) -> int:
    buy, sell = -sys.maxsize, 0
    for price in prices:
        buy = max(buy, sell - price)
        sell = max(sell, price + buy)
    return sell


def max_profit_with_trans(prices: list, trans: int) -> int:
    dp = [[-sys.maxsize, 0] for i in range(trans + 1)]
    for price in prices:
        for i in range(trans, 0, -1):
            dp[i][0] = max(dp[i][0], dp[i - 1][1] - price)
            dp[i][1] = max(dp[i][1], dp[i][0] + price)
    return dp[trans][1]


if __name__ == "__main__":
    res = maxProfit([7, 1, 5, 3, 6, 4])
    print(res)
    res = max_profit_with_trans([3, 3, 5, 0, 0, 3, 1, 4], 2)
    print(res)
    assert res == 6
