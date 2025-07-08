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


def find_occurrence(nums: list, target: int, start: int, end: int, is_first: bool = False) -> int:
    occurrence = -1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] == target:
            occurrence = mid
            if is_first:
                end = mid - 1
            else:
                start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return occurrence


def find_first_last_occurrence(nums: list, target: int) -> []:
    res = [-1, -1]
    first_occurrence = find_occurrence(nums, target, 0, len(nums) - 1, True)
    if first_occurrence != -1:
        res[0] = first_occurrence
        res[1] = find_occurrence(nums, target, first_occurrence, len(nums) - 1)
    return res


if __name__ == "__main__":
    res = binary_search([3, 5, 7, 9, 21, 39], 21)
    print(res)
    res = find_first_last_occurrence([3, 3, 5, 7, 7, 7, 7, 9, 9, 21, 21, 39], 7)
    print(f'First and Last occurrence: {res}')
