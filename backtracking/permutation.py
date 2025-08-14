
def permutation(value: str)-> list:
    value = list(value)
    return permute(value, 0)

def permute(value: list, pos: int):
    result = []
    if pos == len(value) - 1:
        result.append(''.join(value))
        return result
    for index, item in enumerate(value[pos:], start=pos):
        swap(value, index, pos)
        permutation = permute(value, pos+1)
        if permutation:
            result.extend(permutation)
        swap(value, index, pos)
    return result

def swap(value: list, left: int, right: int):
    if left != right:
        value[left], value[right] = value[right], value[left]

if __name__=="__main__":
    res = permutation("abc")
    print(res)