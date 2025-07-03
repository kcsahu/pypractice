def fibonacci(n: int) -> int:
    prev, cur = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1;
    next = 0
    res = [prev, cur]
    for i in range(1, n):
        next = prev + cur
        prev = cur
        cur = next
        res.append(cur)
    return res


if __name__ == "__main__":
    print(fibonacci(7))

