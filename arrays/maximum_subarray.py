from collections import deque


def max_sub_array(nums)-> int:
    max_val = nums[0]
    cur_max = nums[0]
    for i in range(1, len(nums)):
        cur_max = max(nums[i], cur_max + nums[i])
        max_val = max(max_val, cur_max)
    return max_val

def product_sub_array(nums)-> int:
    max_val, min_val, res = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        temp_max = max(nums[i], max(nums[i] * min_val, nums[i] * max_val))
        min_val = min(nums[i], min(nums[i] * min_val, nums[i] * max_val))
        max_val = temp_max
        res = max(res, max_val)
    return res

if __name__ == "__main__":
    print(max_sub_array([-2,-4]))
    print(product_sub_array([2, 3, -2, 4, -3]))
    print(product_sub_array([2, 3, -2, -4, -3]))
