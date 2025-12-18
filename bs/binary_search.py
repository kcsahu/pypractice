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


if __name__ == "__main__":
    res = binary_search([3, 5, 7, 9, 21, 39], 21)
    print(res)
    assert res == 4

