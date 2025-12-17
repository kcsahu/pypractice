## Given an array of non-negative integers arr, you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i],
# check if you can reach any index with value 0.
## Notice that you can not jump outside of the array at any time.
#Input: arr = [4,2,3,0,3,1,2], start = 5
#Output: true
from collections import deque

def can_reach(arr: list[int], start: int)-> bool:
    ## To store the next indices
    dq = deque()
    dq.appendleft(start)
    size = len(arr)
    visited = [False] * size
    while dq:
        index = dq.pop()
        if arr[index] == 0:
            return True
        for next_ind in (index + arr[index], index - arr[index]):
            if 0 <= next_ind < size and not visited[next_ind]:
                dq.appendleft(next_ind)
                visited[next_ind] = True
    return False

if __name__ == "__main__":
    arr = [4,2,3,0,3,1,2]
    res = can_reach(arr, 5)
    print(res)
    assert res

    arr = [3,0,2,1,2]
    res = can_reach(arr, 2)
    print(res)
    assert not res