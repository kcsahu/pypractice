from collections import Counter
def min_window(s: str, t: str)-> str:
    if not s or not t:
        return ''
    min_window = ''
    char_freq = Counter(t)
    cur_window = Counter()
    counter = 0
    left = 0
    for right in range(len(s)):
        right_char = s[right]
        cur_window[right_char] += 1
        if right_char in char_freq and cur_window[right_char] == char_freq[right_char]:
            counter += 1
        
        while counter == len(char_freq):
            if not min_window or len(min_window) > (right - left) +1:
                min_window = s[left: right + 1]
            left_char = s[left]
            cur_window[left_char] -= 1
            if left_char in char_freq and cur_window[left_char] < char_freq[left_char]:
                counter -= 1
            left += 1
    return min_window

if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABCA"
    # res = min_window(s, t)
    print(min_window("ADOBECODEBANC", "ABAC"))

    print(min_window("ADOBECODEBANC", "ABC"))

    print(min_window("bdab", "ab"))
    print(min_window("a", "a"))