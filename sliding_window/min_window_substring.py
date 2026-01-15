# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
# such that every character in t (including duplicates) is included in the window. If there is no such substring,
# return the empty string "".

# The testcases will be generated such that the answer is unique.

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t

from collections import Counter


def min_window1(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)  # required chars
    window = Counter()  # chars in current window
    required = len(need)  # number of unique chars we must satisfy
    formed = 0  # number of characters satisfied so far

    left = 0
    result = ""

    for right in range(len(s)):
        ch = s[right]
        window[ch] += 1

        # A requirement met?
        if ch in need and window[ch] == need[ch]:
            formed += 1

        # Attempt shrinking when valid
        while formed == required:
            # update result if window smaller
            if not result or (right - left + 1) < len(result):
                result = s[left : right + 1]

            # shrink left side
            shrinking_char = s[left]
            window[shrinking_char] -= 1

            # requirement broken?
            if shrinking_char in need and window[shrinking_char] < need[shrinking_char]:
                formed -= 1

            left += 1

    return result


def min_window(s: str, t: str) -> str:
    char_freq = Counter(list(t))
    min_len_window = len(char_freq)
    cur_window = Counter()
    counter = 0
    min_substr = ""
    left = 0
    for right in range(len(s)):
        right_car = s[right]
        cur_window[right_car] = +1

        if right_car in char_freq and cur_window[right_car] == char_freq[right_car]:
            counter += 1

        while counter == min_len_window:
            if not min_substr or right - left + 1 < len(min_substr):
                sub_str = s[left : right + 1]
                min_substr = sub_str
            left_char = s[left]
            cur_window[left_char] -= 1
            if left_char in char_freq and cur_window[left_char] < char_freq[left_char]:
                counter -= 1
            left += 1

    return min_substr


if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABCA"
    # res = min_window(s, t)
    print(min_window("ADOBECODEBANC", "ABAC"))

    print(min_window("ADOBECODEBANC", "ABC"))

    print(min_window("bdab", "ab"))
    print(min_window("a", "a"))
