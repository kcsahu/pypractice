class PermutationString:
    def permutation(self, input: str)-> list:
        nums = list(input)
        result = []
        def permute(pos: int = 0):
            if pos == len(nums) - 1:
                result.append("".join(nums))
                return
            for i in range(pos, len(nums)):
                self.__swap(nums, i, pos)
                permute(pos + 1)
                self.__swap(nums, i, pos)
        permute()
        return result

    def __swap(self, value: list, left: int, right: int):
        if left != right:
           value[left], value[right] = value[right], value[left]

if __name__ == "__main__":
    obj = PermutationString()
    res = obj.permutation("abc")
    print(res)
    assert res == ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']