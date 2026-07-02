# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

def find_median_sorted_arrays(nums1: list[int], nums2: list[int])-> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    nums1_size, nums2_size = len(nums1), len(nums2)
    total_len = (nums1_size + nums2_size)
    mid = (total_len + 1) >> 1
    low, high = 0, nums1_size
    while low <= high:
        i = low + ((high - low) >> 1)
        j = mid - i
        nums1_left = nums1[i-1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < nums1_size else float('inf')
        nums2_left = nums2[j - 1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < nums2_size else float('inf')
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if (total_len % 2):
                return max(nums1_left, nums2_left)
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right))/2
        elif nums1_left > nums2_right:
            high = i - 1
        else:
            low = i + 1

import pytest

@pytest.mark.parametrize("nums1, nums2, expected", [
    # basic odd/even
    ([1, 3], [2, 6, 7], 3.0),
    ([1, 2], [3, 4], 2.5),
    # empty array
    ([], [1, 2, 3], 2.0),
    ([], [1, 2, 3, 4], 2.5),
    ([], [5], 5.0),
    # single elements
    ([1], [2], 1.5),
    ([3], [1, 2, 4], 2.5),
    ([5], [5], 5.0),
    # nums1 larger than nums2 (tests swap)
    ([1, 2, 3, 4], [5], 3.0),
    ([2, 3, 4, 5, 6], [1], 3.5),
    # non-overlapping ranges
    ([1, 2], [3, 4, 5, 6], 3.5),
    ([5, 6], [1, 2, 3, 4], 3.5),
    ([1, 2, 3], [7, 8, 9], 5.0),
    ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),
    # interleaved
    ([1, 3, 5], [2, 4, 6], 3.5),
    ([1, 4, 7], [2, 3, 8, 9], 4.0),
    ([1, 2, 5, 6], [3, 4, 7, 8], 4.5),
    # duplicates
    ([1, 1], [1, 1], 1.0),
    ([1, 2, 2], [2, 3], 2.0),
    ([1, 1, 2], [1, 2, 2], 1.5),
    # negatives
    ([-5, -3, -1], [-4, -2, 0], -2.5),
    ([-3, -1], [-2, 0, 2], -1.0),
    ([-1], [0], -0.5),
    # large gap between values
    ([1], [1000000], 500000.5),
    ([1, 2], [999998, 999999, 1000000], 999998.0),
    # larger arrays
    ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5.5),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
    ([1, 5, 9, 13, 17], [3, 7, 11, 15, 19], 10.0),
])
def test_find_median_sorted_arrays(nums1, nums2, expected):
    assert find_median_sorted_arrays(nums1, nums2) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])