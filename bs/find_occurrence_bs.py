def find_occurrence(nums: list[int], target: int) -> list:
    def search(is_first: bool) -> int:
        start, end = 0, len(nums) - 1
        res = -1
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target:
                res = mid
                if is_first:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return res
    first_occurrence = search(True)

    if first_occurrence != -1:
        last_occurrence = search(False)
        return [first_occurrence, last_occurrence]
    return [-1, -1]

import pytest

class TestFindOccurrence:
    def test_multiple_occurrences(self):
        assert find_occurrence([3, 3, 5, 7, 7, 7, 7, 9, 9, 21, 21, 39], 7) == [3, 6]

    def test_two_occurrences_at_start(self):
        assert find_occurrence([3, 3, 5, 7, 7, 7, 7, 9, 9, 21, 21, 39], 3) == [0, 1]

    def test_single_occurrence(self):
        assert find_occurrence([5, 7, 7, 8, 8, 10], 10) == [5, 5]

    def test_two_occurrences_middle(self):
        assert find_occurrence([5, 7, 7, 8, 8, 10], 8) == [3, 4]

    def test_target_not_found(self):
        assert find_occurrence([5, 7, 7, 8, 8, 10], 3) == [-1, -1]

    def test_single_element_found(self):
        assert find_occurrence([5], 5) == [0, 0]

    def test_single_element_not_found(self):
        assert find_occurrence([5], 3) == [-1, -1]

    def test_all_same_elements_found(self):
        assert find_occurrence([4, 4, 4, 4], 4) == [0, 3]

    def test_all_same_elements_not_found(self):
        assert find_occurrence([4, 4, 4, 4], 5) == [-1, -1]

    def test_target_at_boundaries(self):
        assert find_occurrence([1, 2, 3, 4, 5], 1) == [0, 0]
        assert find_occurrence([1, 2, 3, 4, 5], 5) == [4, 4]
