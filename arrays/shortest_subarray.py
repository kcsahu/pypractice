import sys
from collections import deque
import numpy as np


##Given an integer array nums and an integer k, return the length of the shortest non-empty subarray
# of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array.
# Prefix Sum + Monotonic Deque
def shortest_subarray(nums: list, k: int) -> int:
    size = len(nums)
    prefix_sum = np.zeros(size+1, dtype=np.int32)
    prefix_sum[1:] = np.cumsum(nums)
    # prefix_sum = [0 for i in range(0, size + 1)]
    # for i in range(0, size):
    #     prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    min_len = sys.maxsize
    dq = deque()
    for i in range(0, len(prefix_sum)):
        while dq and prefix_sum[i] - prefix_sum[dq[-1]] >= k:
            min_len = min(min_len, i - dq.pop())
        while dq and prefix_sum[i] <= prefix_sum[dq[0]]:
            dq.popleft()
        dq.appendleft(i)
    return min_len if min_len != sys.maxsize else -1


## Find the minimum size of the sub-array whose sum is equal to or more than the provided target value.
## nums = [2, 3, 1, 2, 4, 3], target=7, res (size of the subarray) =  2 (4 + 3)
## Sliding window + Variable window
def min_subarray_sum(nums: list, target: int) -> int:
    min_len = sys.maxsize
    sum = 0
    j = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        while sum >= target:
            min_len = min(min_len, i - j + 1)
            sum -= nums[j]
            j += 1
    return min_len if min_len != sys.maxsize else 0

## Find the max value of a sub-array for a given size of the sub-array 
# arr = [2, 3, 1, 2, 4, 3], k = 2, Maximum sum of a subarray with size 2 = 7
## Sliding window + Fixed window
def max_sum_subarray(arr: list[int], k: int)-> int:
    max_sum, window_sum = 0, 0
    for i in range(len(arr)):
        window_sum += nums[i]
        if i >= k:
            window_sum -= nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

if __name__ == "__main__":
    ## Min size of Subarray
    nums = [2, 3, 1, 2, 4, 3]
    res = min_subarray_sum(nums, 7)
    print('Minimum Subarray Sum: ',res)
    assert res == 2

    res = shortest_subarray(nums, 7)
    print('Shortest Sub-array: ',res)
    assert res == 2

    nums = [17, 85, 93, -45, -21]
    res = shortest_subarray(nums, 150)
    print('Shortest Sub-array: ',res)
    assert res == 2

    nums = [2, 3, 1, 2, 4, 3]
    res = max_sum_subarray(nums, 2)
    print('Max Sum Subarray: ', res)
