class PermutationNumber:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def permutation(pos: int = 0):
            if pos == len(nums) - 1:
                result.append(list(nums))
                return
            for i in range(pos, len(nums)):
                self.__swap(nums, i, pos)
                permutation(pos + 1)
                self.__swap(nums, i, pos)

        permutation()
        return result

    def __swap(self, value: list, left: int, right: int):
        if left != right:
            value[left], value[right] = value[right], value[left]


if __name__ == "__main__":
    obj = PermutationNumber()
    res = obj.permute([1, 2, 3])
    print(res)
    assert res == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
