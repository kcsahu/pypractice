# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the
# last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the
# police if two adjacent houses were broken into on the same night.
# <p>
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money
# you can rob tonight without alerting the police.
# <p>
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
import sys


def rob(nums: list) -> int:
    size = len(nums)
    dp = [[0 for i in range(2)] for i in range(size)]
    max_rob1, max_rob2 = -sys.maxsize, -sys.maxsize
    for i in range(size):
        if i < size -1:
            dp[i][0] = max(nums[i] + dp[i-2][0] if i>= 2 else nums[i],
                           nums[i] + dp[i-3][0] if i>= 3 else nums[i])
            max_rob1 = max(max_rob1, dp[i][0])
        if i > 0:
            dp[i][1] = max(nums[i] + dp[i-2][1] if i>=2 else nums[i],
                           nums[i] + dp[i-3][1] if i>=3 else nums[i])
            max_rob2 = max(max_rob2, dp[i][1])
    return max(max_rob1, max_rob2)
if __name__=="__main__":
    res = rob([10, 9, 3, 1, 7])
    print(res)
    assert res == 16