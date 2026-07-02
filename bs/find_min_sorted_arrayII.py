# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,4,4,5,6,7] might become:
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# Example 2:
#
# Input: nums = [2,2,2,0,1]
# Output: 0

def find_min(nums: list)-> int:
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + ((end - start) >> 1)
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[end]:
            end = mid
        else:
            end -= 1
    return nums[start]

import pytest

def test_example_with_duplicates():
    assert find_min([2, 2, 2, 0, 1]) == 0

def test_example_trailing_duplicates():
    assert find_min([1, 3, 3]) == 1

def test_no_rotation():
    assert find_min([0, 1, 4, 4, 5, 6, 7]) == 0

def test_rotated_with_duplicate_ends():
    assert find_min([4, 5, 6, 7, 0, 1, 4]) == 0

def test_all_same():
    assert find_min([1, 1, 1, 1]) == 1

def test_single_element():
    assert find_min([5]) == 5

def test_two_elements_rotated():
    assert find_min([2, 1]) == 1

def test_two_same_elements():
    assert find_min([3, 3]) == 3

def test_duplicates_around_pivot():
    assert find_min([3, 3, 1, 3]) == 1

def test_large_duplicate_prefix():
    assert find_min([10, 10, 10, 10, 1, 10]) == 1

def test_negative_numbers():
    assert find_min([0, -1, -1]) == -1

def test_mixed_negative_positive():
    assert find_min([3, 3, -2, -2, 0]) == -2

if __name__ == "__main__":
    pytest.main([__file__, "-v"])