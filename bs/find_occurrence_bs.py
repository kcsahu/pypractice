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
    last_occurrence = search(False)
    if first_occurrence != -1 and last_occurrence != -1:
        return [first_occurrence, last_occurrence]
    return [-1, -1]


if __name__ == "__main__":
    nums = [3, 3, 5, 7, 7, 7, 7, 9, 9, 21, 21, 39]
    res = find_occurrence(nums, 7)
    print('First Occurrence and Last occurrence', res)

    res = find_occurrence(nums, 3)
    print('First Occurrence and Last occurrence', res)

    res = find_occurrence([5,7,7,8,8,10], 8)
    print("First occurrence and Last occurrence: ", res)
