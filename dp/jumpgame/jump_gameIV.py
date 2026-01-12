# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.
# Example:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
from collections import deque, defaultdict


def min_jumps(arr: list[int])-> int:
    dq = deque()
    dq.appendleft(0)
    size = len(arr)
    visited = [False] * size
    counter_map = {}
    counter_map[0] = 0
    graph = defaultdict(deque)
    for ind, val in enumerate(arr):
        graph[val].appendleft(ind)

    while dq:
        index = dq.pop()
        min_jump = counter_map.get(index, 0)
        if index == size - 1:
            return min_jump
        val_dq = graph.get(arr[index])
        while val_dq:
            next_ind = val_dq.pop()
            if index != next_ind and not visited[next_ind]:
                dq.appendleft(next_ind)
                visited[next_ind] = True
                counter_map[next_ind] = min_jump + 1

        for next_ind in (index + 1, index -1):
            if 0 <= next_ind < size and not visited[next_ind]:
                dq.appendleft(next_ind)
                visited[next_ind] = True
                counter_map[next_ind] = min_jump + 1
    return 0

if __name__ =="__main__":
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    min_jump = min_jumps(arr)
    print(min_jump)

