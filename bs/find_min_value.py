def find_min_val(nums: list) -> int:
    """
    Finds the minimum value in a sorted rotated array
    :param nums:
    :return:
    """
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + ((end - start) >> 1)
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
    return nums[start]

def find_min_val_duplicates(nums: list)-> int:
    """
    Finds the minimum value in a sorted rotated array with duplicates
    :param nums:
    :return:
    """
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + ((end - start)>>1)
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[end]:
            end = mid
        else:
            end -= 1
    return nums[start]

if __name__ == "__main__":
    nums = [17, 19, 2, 8, 9, 12]
    res = find_min_val(nums)
    print("Min value: ", res)

    nums = [2, 2, 2, 0, 1, 1, 1, 1, 1]
    res = find_min_val_duplicates(nums)
    print("Min value in duplicates: ",res)
