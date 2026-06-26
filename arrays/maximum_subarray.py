def max_subarray(nums: list) -> int:
   cur_max, max_val = nums[0], nums[0]
   for index in range(1, len(nums)):
       cur_max = max(nums[index], nums[index] + cur_max)
       max_val = max(max_val, cur_max)
   return max_val

class TestMaxSubarray:

    def test_mixed_positive_negative(self):
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_positive(self):
        assert max_subarray([1, 2, 3, 4, 5]) == 15

    def test_all_negative(self):
        assert max_subarray([-3, -1, -2]) == -1

    def test_single_element(self):
        assert max_subarray([7]) == 7

    def test_single_negative_element(self):
        assert max_subarray([-7]) == -7

    def test_large_sum_at_end(self):
        assert max_subarray([-1, -2, 3, 4, 5]) == 12

    def test_large_sum_at_start(self):
        assert max_subarray([5, 4, -1, -10, 1]) == 9

    def test_two_elements_pick_larger(self):
        assert max_subarray([-1, 2]) == 2

    def test_zeros_and_positives(self):
        assert max_subarray([0, 0, 3, 0, 0]) == 3

