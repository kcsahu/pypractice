# There are several consecutive houses along a street, each of which has some money inside.
# There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
#
# The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
#
# You are given an integer array nums representing how much money is stashed in each house. More formally,
# the ith house from the left has nums[i] dollars.
#
# You are also given an integer k, representing the minimum number of houses the robber will steal from.
# It is always possible to steal at least k houses.
#
# Return the minimum capability of the robber out of all the possible ways to steal at least k houses.
#
# Input: nums = [2,3,5,9], k = 2
# Output: 5
# Explanation:
# There are three ways to rob at least 2 houses:
# - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
# - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
# - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
# Therefore, we return min(5, 9, 9) = 5.
import sys


def min_capability(nums: list, k: int):
    max_rob, min_rob = -sys.maxsize, sys.maxsize
    for ind, val in enumerate(nums):
        max_rob = max(max_rob, val)
        min_rob = min(min_rob, val)
    res = max_rob
    while min_rob <= max_rob:
        mid = min_rob + ((max_rob - min_rob) >> 1)
        if __can_rob(nums, mid, k):
            res = mid
            max_rob = mid - 1
        else:
            min_rob = mid + 1
    return res


def __can_rob(nums: list, max_rob: int, k: int):
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


if __name__ == "__main__":
    res = min_capability([2, 7, 9, 3, 1], 2)
    print(res)
    assert res == 2

    res = min_capability([2, 3, 5, 9], 2)
    print(res)
    assert res == 5
