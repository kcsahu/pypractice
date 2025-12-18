from collections import deque
from functools import lru_cache

@lru_cache(10000)
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_DFS(n:int)->int:
    if n == 0:
        return 0
    if n== 1:
        return 1
    dq = deque()
    dq.append(0)
    dq.append(1)
    while n > 1:
        current = dq.pop()
        prev = dq.pop()
        dq.append(current)
        dq.append(current + prev)
        n -= 1
    return dq.pop()


if __name__ == "__main__":
    val = fibonacci(10)
    print(val)

    print(fibonacci_DFS(1000))
