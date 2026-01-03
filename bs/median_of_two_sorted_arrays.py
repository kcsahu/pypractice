# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1: list[int], nums2: list[int])-> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    nums1_size, nums2_size = len(nums1), len(nums2)
    total_len = (nums1_size + nums2_size)
    mid = (total_len + 1) >> 1
    low, high = 0, nums1_size
    while low <= high:
        i = low + ((high - low) >> 1)
        j = mid - i
        nums1_left = nums1[i-1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < nums1_size else float('inf')
        nums2_left = nums2[j - 1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < nums2_size else float('inf')
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if (total_len % 2):
                return max(nums1_left, nums2_left)
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right))/2
        elif nums1_left > nums2_right:
            high = i - 1
        else:
            low = i + 1

if __name__ == "__main__":
    res = findMedianSortedArrays([1, 3], [2, 6 ,7])
    print(res)
    assert res == 3
    res = findMedianSortedArrays([1, 2], [3, 4])
    print(res)
    assert res == 2.5