from functools import lru_cache

@lru_cache(10000)
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    val = fibonacci(8)
    print(val)
