# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def length_of_longest_substring(s: str):
    left, right = 0, 0
    max_len = 0
    visited = set()
    while left < len(s) and right < len(s):
        if s[right] in visited:
            max_len = max(max_len, right - left)
            while left < len(s) and s[right] in visited:
                visited.remove(s[left])
                left += 1
        visited.add(s[right])
        right += 1
    return max(max_len, right - left)


if __name__ == "__main__":
    # obj = Solution()
    res = length_of_longest_substring("bacdabcbb")
    print(res)
    assert res == 4
    res = length_of_longest_substring("dvdf")
    print(res)
    assert res == 3
