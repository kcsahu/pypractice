
def canJump(nums)-> bool:
    max_jump, max_capacity = 0, 0
    for index, num in enumerate(nums):
        max_capacity = max(max_capacity, index + num)
        if max_jump == index:
            max_jump = max_capacity
        if max_jump >= len(nums) - 1:
            return True
    return False

def minJump(nums)-> int:
    max_jump, max_capacity, jump_counter= 0,0,0
    if len(nums) > 1:
        for index, num in enumerate(nums):
            max_capacity = max(max_capacity, index + num)
            if max_jump == index:
                max_jump = max_capacity
                jump_counter += 1
            if max_jump >= len(nums)- 1:
                return jump_counter
    return jump_counter

if __name__ == "__main__":
    res = canJump([2,3,1,1,4])
    print(res)
    assert res
    res = canJump([3,2,1,0,4])
    print(res)
    assert not res
    res = minJump([2,3,1,1,4])
    print(res)
    assert res == 2