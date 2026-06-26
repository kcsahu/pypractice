## Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
## find two numbers such that they add up to a specific target number. Let these two numbers be
## numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
## <p>
## Return the indices of the two numbers, index1 and index2, added by one as an integer array
## [index1, index2] of length 2.
## <p>
## The tests are generated such that there is exactly one solution. You may not use the same element twic
## <p>
## Your solution must use only constant extra space.
## <p>
## Input: numbers = [2,7,11,15], target = 9
## Output: [1,2]
## Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
import pytest


class TwoSum:
    @staticmethod
    def two_sum(nums, target):
        map = {}
        result = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in map.keys():
                result.append((diff, num))
            else:
                map[num] = index
        return result

    @staticmethod
    def two_sum_indices(nums, target):
        map = {}
        result = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in map.keys():
                result.append((index, map.get(diff)))
            else:
                map[num] = index
        return result

class TwoSumII:
    @staticmethod
    def two_sum_bs(nums, target):
        ## nums is sorted
        end = len(nums) - 1
        res = []
        for index, num in enumerate(nums):
            diff = target - num
            search = TwoSumII.search(nums, index + 1, end, diff)
            if search != -1:
                res.append(index + 1)
                res.append(search + 1)
                return res
        return res

    @staticmethod
    def search(nums, start, end, target):
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

def two_sum(nums: list, target: int)-> list:
    map = {}
    for i,val in enumerate(nums):
        diff = target - val
        if diff not in map.keys():
            map[val] = i
        else:
            ind = map.get(diff)
            return [ind, i]
    return []


# ── Tests ──────────────────────────────────────────────────────────────────

class TestTwoSumPairs:
    def test_basic(self):
        assert TwoSum.two_sum([2, 7, 11, 15], 9) == [(2, 7)]

    def test_multiple_pairs(self):
        result = TwoSum.two_sum([1, 2, 3, 4], 5)
        assert (2, 3) in result
        assert (1, 4) in result

    def test_no_pair(self):
        assert TwoSum.two_sum([1, 2, 3], 10) == []

    def test_negative_numbers(self):
        assert TwoSum.two_sum([-3, 0, 3], 0) == [(-3, 3)]

    def test_duplicates(self):
        assert TwoSum.two_sum([3, 3], 6) == [(3, 3)]

    def test_single_element(self):
        assert TwoSum.two_sum([5], 5) == []

    def test_empty(self):
        assert TwoSum.two_sum([], 0) == []


class TestTwoSumIndices:
    def test_basic(self):
        assert TwoSum.two_sum_indices([2, 7, 11, 15], 9) == [(1, 0)]

    def test_multiple_pairs(self):
        result = TwoSum.two_sum_indices([1, 2, 3, 4], 5)
        assert (2, 1) in result
        assert (3, 0) in result

    def test_no_pair(self):
        assert TwoSum.two_sum_indices([1, 2, 3], 10) == []

    def test_negative_numbers(self):
        assert TwoSum.two_sum_indices([-3, 0, 3], 0) == [(2, 0)]

    def test_empty(self):
        assert TwoSum.two_sum_indices([], 5) == []


class TestTwoSumIIBinarySearch:
    def test_basic(self):
        assert TwoSumII.two_sum_bs([2, 7, 11, 15], 9) == [1, 2]

    def test_last_two_elements(self):
        assert TwoSumII.two_sum_bs([1, 3, 5, 7], 12) == [3, 4]

    def test_first_two_elements(self):
        assert TwoSumII.two_sum_bs([1, 2, 5, 9], 3) == [1, 2]

    def test_two_element_array(self):
        assert TwoSumII.two_sum_bs([1, 2], 3) == [1, 2]

    def test_no_pair(self):
        assert TwoSumII.two_sum_bs([1, 2, 3], 10) == []

    def test_returns_one_indexed(self):
        result = TwoSumII.two_sum_bs([2, 7, 11, 15], 9)
        assert result[0] >= 1 and result[1] >= 1

    def test_negative_numbers(self):
        assert TwoSumII.two_sum_bs([-5, -3, 0, 2, 8], -3) == [1, 4]


class TestBinarySearch:
    def test_found_middle(self):
        assert TwoSumII.search([2, 7, 11, 15], 0, 3, 7) == 1

    def test_not_found(self):
        assert TwoSumII.search([1, 2, 3], 0, 2, 99) == -1

    def test_first_element(self):
        assert TwoSumII.search([1, 3, 5, 7], 0, 3, 1) == 0

    def test_last_element(self):
        assert TwoSumII.search([1, 3, 5, 7], 0, 3, 7) == 3

    def test_restricted_range_excludes_target(self):
        assert TwoSumII.search([1, 3, 5, 7], 2, 3, 1) == -1


class TestModuleLevelTwoSum:
    def test_basic(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_middle_elements(self):
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_duplicate_values(self):
        assert two_sum([3, 3], 6) == [0, 1]

    def test_no_pair(self):
        assert two_sum([1, 2, 3], 10) == []

    def test_negative_numbers(self):
        assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    def test_empty(self):
        assert two_sum([], 5) == []

    def test_single_element(self):
        assert two_sum([5], 5) == []
