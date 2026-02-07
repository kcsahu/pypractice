
def permutation(value: str)-> list:
    value = list(value)
    result = []

    def backtrack(val, pos:int =0):
        if pos == len(val):
            result.append(''.join(value))
            return
        for i in range(pos, len(val)):
            val[i], val[pos] = val[pos], val[i]
            backtrack(val, pos + 1)
            val[i], val[pos] = val[pos], val[i]
    backtrack(value)
    return result

def permute(value: list, pos: int = 0)-> list:
    def swap(val: list, left: int, right: int):
        if left != right:
            val[left], val[right] = val[right], val[left]
    result = []
    if pos == len(value) - 1:
        result.append(''.join(value))
    for i, val in enumerate(value[pos:]):
        swap(value, i, pos)
        next_val = permute(value, pos + 1)
        result.extend(next_val)
        swap(value, i, pos)
    return result


if __name__=="__main__":
    res = permutation("abc")
    print(res)

    res = permutation('abcd')
    print(res)