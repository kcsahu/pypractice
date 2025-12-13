
def knapsack(values: list, capacity: int, wts: list)-> int:
    dp = [0 for i in range(capacity + 1)]
    for ind, val in enumerate(values):
        for w in range(capacity, wts[ind] - 1, -1):
            dp[w] = max(dp[w], val + dp[w - wts[ind]])
    return dp[capacity]




if __name__== "__main__":
    res = knapsack([1, 8, 22, 28, 18], 11, [1, 3, 6, 7, 5])
    print(res)
    assert res == 40
