# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
## Example 1:

#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.

#Example 2:
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# The overall run time complexity should be O(log (m+n)).

def find_median_sorted_arrays(nums1: list[int], nums2: list[int])-> float:
    # Binary-search the shorter array so the search takes O(log(min(m, n)))
    # time and the partition indices always stay within a small range.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    nums1_size, nums2_size = len(nums1), len(nums2)
    total_len = (nums1_size + nums2_size)
    # The left partition gets the extra element when the combined length is odd.
    mid = (total_len + 1) >> 1
    low, high = 0, nums1_size
    while low <= high:
        # i elements from nums1 and j from nums2 make up the left partition.
        # Choosing i determines j because the left side must contain `mid` items.
        i = low + ((high - low) >> 1)
        j = mid - i
        # Values just outside an array's ends act as sentinels, avoiding separate
        # boundary cases when a partition takes none or all of an array.
        nums1_left = nums1[i-1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < nums1_size else float('inf')
        nums2_left = nums2[j - 1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < nums2_size else float('inf')
        # A valid partition has every left-side value <= every right-side value.
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if (total_len % 2):
                # For odd length, the largest value on the left is the median.
                return max(nums1_left, nums2_left)
            # For even length, average the largest left and smallest right values.
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right))/2
        elif nums1_left > nums2_right:
            # Too many nums1 values are on the left; move its cut left.
            high = i - 1
        else:
            # nums2_left > nums1_right: move nums1's cut right to balance sides.
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
