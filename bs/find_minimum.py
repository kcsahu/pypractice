# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
# the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

def find_min(nums: list) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + ((end - start) >> 1)
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
    return nums[start]


def test_rotated_3_times():
    assert find_min([3, 4, 5, 1, 2]) == 1


def test_rotated_4_times():
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0


def test_not_rotated():
    assert find_min([0, 1, 2, 4, 5, 6, 7]) == 0


def test_single_element():
    assert find_min([1]) == 1


def test_two_elements_rotated():
    assert find_min([2, 1]) == 1


def test_two_elements_not_rotated():
    assert find_min([1, 2]) == 1


def test_rotated_once():
    assert find_min([5, 1, 2, 3, 4]) == 1


def test_minimum_at_end():
    assert find_min([2, 3, 4, 5, 1]) == 1
