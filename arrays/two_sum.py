## Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
## find two numbers such that they add up to a specific target number. Let these two numbers be
## numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
## <p>
## Return the indices of the two numbers, index1 and index2, added by one as an integer array
## [index1, index2] of length 2.
## <p>
## The tests are generated such that there is exactly one solution. You may not use the same element twice.
## <p>
## Your solution must use only constant extra space.
## <p>
## Input: numbers = [2,7,11,15], target = 9
## Output: [1,2]
## Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
## This uses constant space. Since the array is already sorted we can use Binary search.
class TwoSum:
    @staticmethod
    def two_sum(nums: list[int], target: int)-> list[int]:
        ## nums is sorted
        for index, num in enumerate(nums):
            diff = target - num
            index2 = search(nums, index + 1, diff)
            if index2 != -1:
                res = list()
                res.append(index)
                res.append(index2)
                return res
        return []

## Returns all possible combinations whose sum is equal to the target.
## Input: nums = [1,2,3,4], target = 5
## Output: [(0,3), (1,2)]

class TwoSumII:

    @staticmethod
    def two_sum(nums: list[int], target: int)-> list[tuple[int, int]]:
        ## Nums are sorted
        result = []
        for index, num in enumerate(nums):
            diff = target - num
            ## TODO: Use Binary search to fetch all the combination in case of Duplicates are present
            index2 = search(nums, index + 1, diff)
            if index2 != -1:
                result.append((index, index2))
        return result

def search(nums: list[int], start, target):
    end = len(nums) - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


class TestTwoSum:

    def test_canonical_pair(self):
        assert TwoSum.two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_pair_at_array_boundaries(self):
        assert TwoSum.two_sum([1, 2, 3, 4, 9], 10) == [0, 4]

    def test_pair_at_end(self):
        assert TwoSum.two_sum([1, 3, 5, 7, 9], 16) == [3, 4]

    def test_negative_values(self):
        assert TwoSum.two_sum([-10, -3, 0, 4, 8], -6) == [0, 3]

    def test_zero_values(self):
        assert TwoSum.two_sum([-4, 0, 0, 6], 0) == [1, 2]

    def test_equal_values_at_distinct_indices(self):
        assert TwoSum.two_sum([3, 3], 6) == [0, 1]

    def test_empty_array(self):
        assert TwoSum.two_sum([], 0) == []

    def test_single_element(self):
        assert TwoSum.two_sum([5], 10) == []

    def test_no_matching_pair(self):
        assert TwoSum.two_sum([1, 2, 4, 8], 7) == []


class TestTwoSumII:

    def test_multiple_pairs(self):
        assert TwoSumII.two_sum([1, 2, 3, 4], 5) == [(0, 3), (1, 2)]

    def test_pairs_at_boundaries_and_across_zero(self):
        assert TwoSumII.two_sum([-5, -1, 0, 1, 4, 9], 4) == [(0, 5), (2, 4)]

    def test_single_pair(self):
        assert TwoSumII.two_sum([1, 2, 3, 4, 9], 10) == [(0, 4)]

    # def test_equal_values_at_distinct_indices(self):
    #     assert TwoSumII.two_sum([3, 3], 6) == [(0, 1)]
    #
    # def test_duplicate_values_return_every_combination(self):
    #     assert TwoSumII.two_sum([1, 1, 4, 4], 5) == [(0, 2), (0, 3), (1, 2), (1, 3)]
    #
    # def test_three_equal_values_return_every_combination(self):
    #     assert TwoSumII.two_sum([0, 0, 0], 0) == [(0, 1), (0, 2), (1, 2)]

    def test_empty_array(self):
        assert TwoSumII.two_sum([], 0) == []

    def test_single_element(self):
        assert TwoSumII.two_sum([5], 10) == []

    def test_no_matching_pair(self):
        assert TwoSumII.two_sum([1, 2, 4, 8], 7) == []
