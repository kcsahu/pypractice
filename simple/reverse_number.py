

def reverse(val: int)-> int:
    reverse = 0
    while val > 0:
        x = val % 10
        reverse = reverse * 10 + x
        val = val // 10
    return reverse

if __name__ == "__main__":
    res = reverse(1234)
    print(res)
