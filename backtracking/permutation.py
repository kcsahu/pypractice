
def permutation(value: str)-> list:
    value = list(value)
    return permute(value)

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