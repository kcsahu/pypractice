import sys


def max_profit(prices: list, fee: int)-> int:
    buy, max_profit = -sys.maxsize, 0
    for ind, price in enumerate(prices):
        buy = max(buy, max_profit - price)
        max_profit = max(max_profit, buy + price - fee)
    return max_profit


if __name__=="__main__":
    res = max_profit([1, 3, 7, 5, 10, 3], 3)
    print(res)
    assert res == 6