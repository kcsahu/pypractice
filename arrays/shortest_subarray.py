import sys
from collections import deque

import numpy as np

# Prefix Sum + Monotonic Deque
##Given an integer array nums and an integer k, return the length of the shortest non-empty subarray
# of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array.

def shortest_subarray(nums: list, k: int) -> int:
    size = len(nums)
    min_length = sys.maxsize
    prefix_sum = np.zeros(size + 1, dtype=np.int32)
    prefix_sum[1:] = np.cumulative_sum(nums)
    # for i in range(0, size):
    #     prefix_sum[i + 1] = nums[i] + prefix_sum[i]
    dq = deque()
    for i in range(0, len(prefix_sum)):
        while len(dq) > 0 and prefix_sum[i] - prefix_sum[dq[-1]] >= k:
            min_length = min(min_length, i - dq.pop())
        while len(dq) > 0 and prefix_sum[i] < prefix_sum[dq[0]]:
            dq.popleft()
        dq.appendleft(i)
    return min_length if min_length != sys.maxsize else -1


## Sliding window + Variable window
## Find the minimum size of the sub-array whose sum is equal to or more than the provided target value.
## nums = [2, 3, 1, 2, 4, 3], target=7, res (size of the subarray) =  2 (4 + 3)
def min_subarray_sum(nums: list, target: int) -> int:
    prefix_sum, left_ind, min_len = 0, 0, sys.maxsize
    for ind, val in enumerate(nums):
        prefix_sum = prefix_sum + val
        while prefix_sum >= target:
            min_len = min(min_len, ind - left_ind + 1)
            prefix_sum = prefix_sum - nums[left_ind]
            left_ind += 1
    return min_len if min_len != sys.maxsize else -1

## Sliding window + Fixed window
## Find the max value of a sub-array for a given size of the sub-array
# arr = [2, 3, 1, 2, 4, 3], k = 2, Maximum sum of a subarray with size 2 = 7
def max_sum_subarray(arr: list[int], k: int) -> int:
    max_val, window_sum = 0, 0
    for ind, val in enumerate(arr):
        window_sum = window_sum + val
        if ind >= k:
            window_sum -= arr[ind - k]
        max_val = max(max_val, window_sum)
    return max_val


class TestShortestSubarray:

    def test_basic(self):
        assert shortest_subarray([17, 85, 93, -45, -21], 150) == 2

    def test_single_element_meets_k(self):
        assert shortest_subarray([5, 1, 1], 5) == 1

    def test_window_in_middle(self):
        assert shortest_subarray([1, 2, 3, 4, 5], 9) == 2

    def test_no_valid_subarray(self):
        assert shortest_subarray([1, 2, 3], 100) == -1

    def test_all_negative(self):
        assert shortest_subarray([-1, -2, -3], 1) == -1


class TestMinSubarraySum:

    def test_basic(self):
        assert min_subarray_sum([2, 3, 1, 2, 4, 3], 7) == 2

    def test_single_element_meets_target(self):
        assert min_subarray_sum([1, 4, 4], 4) == 1

    def test_whole_array_needed(self):
        assert min_subarray_sum([1, 2, 3, 4, 5], 15) == 5

    def test_no_valid_subarray(self):
        assert min_subarray_sum([1, 1, 1, 1, 1], 11) == -1

    def test_first_element_sufficient(self):
        assert min_subarray_sum([5, 5, 5], 3) == 1


class TestMaxSumSubarray:

    def test_basic(self):
        assert max_sum_subarray([2, 3, 1, 2, 4, 3], 2) == 7

    def test_window_size_one(self):
        assert max_sum_subarray([1, 2, 3, 4, 5], 1) == 5

    def test_window_equals_array_length(self):
        assert max_sum_subarray([1, 2, 3, 4, 5], 5) == 15

    def test_window_in_middle(self):
        assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9

    def test_window_at_end(self):
        assert max_sum_subarray([3, 1, 2, 5], 2) == 7
