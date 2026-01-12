import sys
import numpy as np
def max_profit(prices: list[int], k: int)-> int:
    dp = np.zeros((k+1, 2), dtype='int64')
    dp[:, 0] = -sys.maxsize
    for i, price in enumerate(prices):
        for j in range(k, 0, -1):
            dp[j, 0] = max(dp[j, 0], dp[j-1, 1] - price)
            dp[j, 1] = max(dp[j, 1], dp[j, 0] + price)
    return dp[k, 1]



if __name__=="__main__":
    res = max_profit([3, 3, 5, 0, 0, 3, 1, 4], 2)
    print(res)
    assert res == 6