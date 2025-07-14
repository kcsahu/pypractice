class Permutation:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.permutation(nums, 0, result)
        return result

    def permutation(self, nums, pos, result):
        if pos == len(nums) - 1:
            result.append(list(nums))
            return
        for index in range(pos, len(nums)):
            self.swap(nums, pos, index)
            self.permutation(nums, pos + 1, result)
            self.swap(nums, pos, index)

    def swap(self, nums, left, right):
        if left != right:
            nums[left], nums[right] = nums[right], nums[left]

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = set()
        self.permutationUnique(nums, 0, result)
        return [list(item) for item in result]

    def permutationUnique(self, nums, pos, result):
        if pos == len(nums)-1:
            result.add(tuple(nums))
            return
        for index in range(pos, len(nums)):
            self.swap(nums, pos, index)
            self.permutationUnique(nums, pos + 1, result)
            self.swap(nums, pos, index)

if __name__ == "__main__":
    obj = Permutation()
    res = obj.permute([1, 2, 3])
    print(res)
    res = obj.permuteUnique([2,2,1,1])
    print(res)
