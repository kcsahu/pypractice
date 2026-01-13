from collections import deque

def max_sub_array(nums)-> int:
    max_val = nums[0]
    cur_max = nums[0]
    for i in range(1, len(nums)):
        cur_max = max(nums[i], cur_max + nums[i])
        max_val = max(max_val, cur_max)
    return max_val

def product_sub_array(nums)-> int:
    max_val, min_val, result = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        cur_max = max(nums[i], max(nums[i] * min_val, nums[i] * max_val))
        min_val = min(nums[i], min(nums[i] * min_val, nums[i] * max_val))
        max_val = cur_max
        result = max(result, max_val)
    return result

if __name__ == "__main__":
    res = max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
    assert res == 6
    print(product_sub_array([2, 3, -2, 4, -3]))
    print(product_sub_array([2, 3, -2, -4, -3]))
