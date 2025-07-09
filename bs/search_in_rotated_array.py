def search(nums: list, target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def search_in_duplicates(nums: list, target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[start] < nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif nums[mid] < nums[end]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        elif nums[start] == nums[mid]:
            start += 1
        else:
            end -= 1
    return -1


if __name__ == "__main__":
    res = search([4, 5, 6, 7, 0, 1, 2], 0)
    print("Searched position: ", res)

    res = search_in_duplicates([4, 5, 5, 6, 7, 7, 0, 1, 2], 7)
    print("Search position with duplicates: ", res)
