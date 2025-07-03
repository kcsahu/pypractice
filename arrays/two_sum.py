## Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
## find two numbers such that they add up to a specific target number. Let these two numbers be
## numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
## <p>
## Return the indices of the two numbers, index1 and index2, added by one as an integer array
## [index1, index2] of length 2.
## <p>
## The tests are generated such that there is exactly one solution. You may not use the same element twic
## <p>
## Your solution must use only constant extra space.
## <p>
## Input: numbers = [2,7,11,15], target = 9
## Output: [1,2]
## Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
class TwoSum:
    @staticmethod
    def two_sum(nums, target):
        map = {}
        result = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in map.keys():
                result.append((diff, num))
            else:
                map[num] = index
        return result

    @staticmethod
    def two_sum_indices(nums, target):
        map = {}
        result = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in map.keys():
                result.append((index, map.get(diff)))
            else:
                map[num] = index
        return result

class TwoSumII:
    @staticmethod
    def two_sum_bs(nums, target):
        ## nums is sorted
        end = len(nums) - 1
        res = []
        for index, num in enumerate(nums):
            diff = target - num
            search = TwoSumII.search(nums, index + 1, end, diff)
            if search != -1:
                res.append(index + 1)
                res.append(search + 1)
                return res
        return res

    @staticmethod
    def search(nums, start, end, target):
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

if __name__ == "__main__":
    res = TwoSum.two_sum([2, 7, 8, 14], 9)
    print(res)
    res = TwoSum.two_sum_indices([3, 2, 4, 0, 1, 5, 6], 6)
    print(res)

    res = TwoSumII.two_sum_bs([2, 7, 11, 15], 9)
    print(res)