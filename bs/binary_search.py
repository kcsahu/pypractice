def binary_search(nums: list, target: int) -> int:
    start, end = 0, len(nums) - 1
    while (start <= end):
        mid = start + ((end - start) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def test_target_found_middle():
    assert binary_search([3, 5, 7, 9, 21, 39], 21) == 4


def test_target_found_first():
    assert binary_search([1, 3, 5, 7], 1) == 0


def test_target_found_last():
    assert binary_search([1, 3, 5, 7], 7) == 3


def test_target_not_found():
    assert binary_search([1, 3, 5, 7], 4) == -1


def test_single_element_found():
    assert binary_search([42], 42) == 0


def test_single_element_not_found():
    assert binary_search([42], 1) == -1


def test_empty_list():
    assert binary_search([], 5) == -1


def test_negative_numbers():
    assert binary_search([-10, -5, 0, 3, 8], -5) == 1


def test_duplicates_returns_a_valid_index():
    result = binary_search([1, 2, 2, 2, 3], 2)
    assert result in [1, 2, 3]


