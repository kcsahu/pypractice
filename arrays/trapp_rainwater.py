## ## ###  Two pointers  ###
##
## Given n non-negative integers representing an elevation map where the width of each bar is 1,
## compute how much water it can trap after raining.
##
## Input: height = [4,2,0,3,2,5]
## Output: 9

def trap_rainwater(height: list) -> int:
    trapped_water = 0
    left_ind, left_max, right_ind, right_max = 0, 0, len(height) - 1, 0
    while left_ind < right_ind:
        if height[left_ind] < height[right_ind]:
            if height[left_ind] >= left_max:
                left_max = height[left_ind]
            else:
                trapped_water += left_max - height[left_ind]
            left_ind += 1
        else:
            if height[right_ind] >= right_max:
                right_max = height[right_ind]
            else:
                trapped_water += right_max - height[right_ind]
            right_ind -= 1
    return trapped_water

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = trap_rainwater(height)
    print(res)
    assert res == 6

    height=[4,2,0,3,2,5]
    res = trap_rainwater(height)
    print(res)
    assert res == 9

