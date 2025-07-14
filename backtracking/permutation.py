
def permutation(value: str)-> list:
    value = list(value)
    return permute(value, 0)

def permute(value: list, pos: int):
    if pos == len(value) - 1:
        return ''.join(value)
    result = []
    for index in range(pos, len(value)):
        swap(value, index, pos)
        permutation = permute(value, pos+1)
        if isinstance(permutation, list):
            result.extend(permutation)
        else:
            result.append(permutation)
        swap(value, index, pos)
    return result

def swap(value: list, left: int, right: int):
    if left != right:
        value[left], value[right] = value[right], value[left]

if __name__=="__main__":
    res = permutation("abc")
    print(res)