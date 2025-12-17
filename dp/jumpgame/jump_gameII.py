# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# <p>
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
# if you are at nums[i], you can jump to any nums[i + j] where:
# <p>
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can
# reach nums[n - 1].
# <p>
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
# then 3 steps to the last index.

def min_jump(nums: list[int])-> int:
    max_jump, jump_capacity, jump_count = 0,0,0
    for ind, num in enumerate(nums):
        jump_capacity = max(jump_capacity, num + ind)
        if max_jump == ind:
            max_jump = jump_capacity
            jump_count += 1
        if max_jump >= len(nums)-1:
            return jump_count
    return -1

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    res = min_jump(nums)
    print(res)
    assert res == 2
