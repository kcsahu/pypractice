

def permutation(s: str)-> list[str]:
    result = []

    def backtrack(input: list, pos: int = 0):
        if pos == len(input):
            result.append(''.join(input))
            return
        for i in range(pos, len(input)):
            input[i], input[pos] = input[pos], input[i]
            backtrack(input, pos + 1)
            input[i], input[pos] = input[pos], input[i]
    if s:
        input = list(s)
        backtrack(input)
    return result

if __name__=="__main__":
    s = 'abc'
    result = permutation(s)
    print(result)