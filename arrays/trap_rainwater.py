## ## ###  Two pointers  ###
##
## Given n non-negative integers representing an elevation map where the width of each bar is 1,
## compute how much water it can trap after raining.
##
## Input: height = [4,2,0,3,2,5]
## Output: 9

def trap_rainwater(height: list) -> int:
    trap_water = 0
    left_max, left_ind, right_max, right_ind = 0, 0, 0, len(height) - 1
    while left_ind < right_ind:
        if height[left_ind] < height[right_ind]:
            if left_max > height[left_ind]:
                trap_water += left_max - height[left_ind]
            else:
                left_max = height[left_ind]
            left_ind += 1
        else:
            if right_max > height[right_ind]:
                trap_water += right_max - height[right_ind]
            else:
                right_max = height[right_ind]
            right_ind -= 1
    return trap_water


class TestTrapRainwater:

    def test_basic(self):
        assert trap_rainwater([4, 2, 0, 3, 2, 5]) == 9

    def test_leetcode_classic(self):
        assert trap_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_symmetric_valley(self):
        assert trap_rainwater([3, 0, 3]) == 3

    def test_water_both_sides(self):
        assert trap_rainwater([3, 1, 2, 4, 0, 1, 3, 2]) == 8

    def test_monotonically_increasing_no_water(self):
        assert trap_rainwater([1, 2, 3, 4, 5]) == 0

    def test_monotonically_decreasing_no_water(self):
        assert trap_rainwater([5, 4, 3, 2, 1]) == 0

    def test_flat_no_water(self):
        assert trap_rainwater([3, 3, 3]) == 0

    def test_single_element(self):
        assert trap_rainwater([5]) == 0

    def test_two_elements(self):
        assert trap_rainwater([1, 2]) == 0

    def test_all_zeros(self):
        assert trap_rainwater([0, 0, 0]) == 0
