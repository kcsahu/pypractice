import sys
from collections import deque


def shorted_subarray(nums, k):
    size = len(nums)
    prefix_sum = [0 for i in range(size+1)]
    for i in range(0, size):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    min_len = sys.maxsize
    my_dq = deque()
    for index in range(len(prefix_sum)):
        while len(my_dq) > 0 and prefix_sum[index] - prefix_sum[my_dq[-1]] >= k:
            min_len = min(min_len, index - my_dq.pop())
        while len(my_dq) > 0 and prefix_sum[index] <= prefix_sum[my_dq[0]]:
            my_dq.popleft()
        my_dq.appendleft(index)
    return min_len if min_len != sys.maxsize else -1


if __name__ == "__main__":
    nums = [1,2]
    res = shorted_subarray(nums, 4)
    print(res)

