import sys


## House Robber IV
def min_capability(nums: list, k: int) -> int:
    size = len(nums)
    min_val, max_val = sys.maxsize, -sys.maxsize
    for num in nums:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    res = max_val
    while min_val <= max_val:
        mid = min_val + ((max_val - min_val) >> 1)
        if can_rob(nums, mid, k):
            res = mid
            max_val = mid - 1
        else:
            min_val = mid + 1
    return res


def can_rob(nums, max_rob, k) -> bool:
    size, i = len(nums), 0
    while i < size:
        if nums[i] <= max_rob:
            i += 2
            k -= 1
        else:
            i += 1
        if k == 0:
            return True
    return False


def rob(nums: list) -> int:
    max_rob = 0
    for i in range(0, len(nums)):
        nums[i] = max(nums[i] + nums[i - 2] if i >= 2 else nums[i],
                      nums[i] + nums[i - 3] if i >= 3 else nums[i])
        max_rob = max(nums[i], max_rob)
    return max_rob

def rob2(nums: list) -> int:
    size = len(nums)
    dp = [[0 for x in range(2)] for x in range(size)]
    left_max, right_max = 0,0
    for i in range(size):
        if i < size - 1:
            dp[i][0] = max(nums[i] + dp[i-2][0] if i >= 2 else nums[i],
                           nums[i] + dp[i-3][0] if i>=3 else nums[i])
            left_max = max(dp[i][0], left_max)
        if i > 0:
            dp[i][1] = max(nums[i] + dp[i-2][1] if i>=2 else nums[i],
                           nums[i] + dp[i-3][1] if i>=3 else nums[i])
            right_max = max(dp[i][1], right_max)
    return max(left_max, right_max)



if __name__ == "__main__":
    res = rob([2, 7, 9, 3, 1])
    print("House Robber-I result: ",res)
    res = rob2([10, 9, 3, 1, 7])
    print("House Robber-II result: ", res)
    res = min_capability([2, 7, 9, 3, 1], 2)
    print("House Robber-IV result: ", res)
