import numpy as np
import sys

def rob(nums: list[int]) -> int:
    max_rob = -sys.maxsize
    size = len(nums)
    dp = np.zeros((size, 2), dtype="int")
    for i in range(size):
        if i > 0:
            dp[i, 0] = max(
                nums[i] + dp[i - 2, 0] if i >= 2 else nums[i],
                nums[i] + dp[i - 3, 0] if i >= 3 else nums[i],
            )
            max_rob = max(max_rob, dp[i, 0])
        if i < size:
            dp[i, 1] = max(
                nums[i] + dp[i - 2, 0] if i >= 2 else nums[i],
                nums[i] + dp[i - 3, 1] if i >= 3 else nums[i],
            )
            max_rob = max(max_rob, dp[i, 1])
    return max_rob


if __name__ == "__main__":
    res = rob([10, 9, 3, 1, 7])
    print(res)
    assert res == 16
