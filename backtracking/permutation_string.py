

class PermutationString:
    iteration = 0
    def permutation(self, value) -> list:
        result = []
        self.permute(list(value), 0, result)
        return result

    def permute(self, value: list, pos: int, result: list):
        if pos == len(value) - 1:
            result.append("".join(value))
            return
        for index in range(pos, len(value)):
            self.swap(value, index, pos)
            self.permute(value, pos + 1, result)
            self.swap(value, index, pos)
            self.iteration += 1

    def swap(self, value: list, left: int, right: int):
        if left != right:
           value[left], value[right] = value[right], value[left]

if __name__ == "__main__":
    obj = PermutationString()
    res = obj.permutation("abc")
    print(obj.iteration)
    print(res)