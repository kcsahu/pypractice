# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# <p>
# Return true if you can reach the last index, or false otherwise.
# <p>
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

def can_jump(nums: list[int])-> bool:
    max_jump, jump_capacity = 0,0
    for ind, num in enumerate(nums):
        jump_capacity = max(jump_capacity, num + ind)
        if max_jump == ind:
            max_jump = jump_capacity
        if max_jump >= len(nums) - 1:
            return True
    return False

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    res = can_jump(nums)
    print(res)
    assert res