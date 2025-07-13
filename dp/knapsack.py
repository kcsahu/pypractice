
def knapsack(values: list, capacity: int, wts: list)-> int:
    dp = [0 for _ in range(capacity + 1)]
    for index, value in enumerate(values):
        for w in range(capacity, wts[index] -1, -1):
            dp[w] = max(dp[w], value + dp[w - wts[index]])
    return dp[capacity]

if __name__== "__main__":
    res = knapsack([1, 8, 22, 28, 18], 11, [1, 3, 6, 7, 5])
    print(res)
    assert res == 40
