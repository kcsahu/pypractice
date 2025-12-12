from collections import deque
from functools import lru_cache

@lru_cache(10000)
def fibonaci(n: int)-> int:
    if n == 0:
        return 0;
    elif n < 2:
        return 1
    return fibonaci(n - 1) + fibonaci( n-2)



if __name__=="__main__":
    val = fibonaci(100)
    print(val)