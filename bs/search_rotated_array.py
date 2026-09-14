def search(nums: list[int], target: int) -> int:
    """Return a target index from a rotated, strictly increasing array."""
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[start] > nums[mid]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

def search_with_duplicates(nums: list[int], target: int) -> bool:
    """Return whether target occurs in a rotated non-decreasing array."""
    start, end = 0, len(nums)-1
    while start <= end:
        mid = start +((end - start)>>1)
        if nums[mid] == target:
            return True
        elif nums[start] > nums[mid]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        elif nums[start] < nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif nums[start] == nums[mid]:
            start += 1
    return False


class TestSearch:

    def test_target_in_right_sorted_half(self):
        assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_target_in_left_sorted_half(self):
        assert search([4, 5, 6, 7, 0, 1, 2], 6) == 2

    def test_target_not_found(self):
        assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_not_rotated_array(self):
        assert search([1, 3, 5, 7, 9], 7) == 3

    def test_rotation_at_last_position(self):
        assert search([2, 3, 4, 5, 1], 1) == 4

    def test_empty_array(self):
        assert search([], 1) == -1

    def test_single_element_found_and_absent(self):
        assert search([42], 42) == 0
        assert search([42], 7) == -1

    def test_all_two_element_rotations(self):
        assert search([1, 2], 1) == 0
        assert search([1, 2], 2) == 1
        assert search([2, 1], 2) == 0
        assert search([2, 1], 1) == 1


class TestSearchWithDuplicates:

    def test_target_present_with_duplicate_values(self):
        assert search_with_duplicates([2, 5, 6, 0, 0, 1, 2], 0)

    def test_target_absent_with_duplicate_values(self):
        assert not search_with_duplicates([2, 5, 6, 0, 0, 1, 2], 3)

    def test_ambiguous_half_due_to_duplicate_endpoints(self):
        assert search_with_duplicates([1, 1, 1, 3, 1], 3)

    def test_all_values_equal(self):
        assert search_with_duplicates([1, 1, 1, 1], 1)
        assert not search_with_duplicates([1, 1, 1, 1], 2)

    def test_single_element_found_and_absent(self):
        assert search_with_duplicates([5], 5)
        assert not search_with_duplicates([5], 1)

    def test_empty_array(self):
        assert not search_with_duplicates([], 1)

    def test_duplicate_values_across_the_rotation_pivot(self):
        assert search_with_duplicates([1, 3, 1, 1, 1], 3)
