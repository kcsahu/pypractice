# You are given a string s and an array of strings words. All the strings of words are of the same length.
#
# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
#
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
# are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of
# any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in
# any order.
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
#
# Output: [0,9]
#
# Explanation:
#
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
from collections import defaultdict, Counter


# TODO use sliding window
def find_substring(s: str, words: list):
    size, word_size = len(words), len(words[0])
    total_size = word_size * size
    word_map = defaultdict(int)
    for word in words:
        word_map[word] += 1

    def is_substring(s: str) -> bool:
        word_dict = defaultdict(int)
        word_count = 0
        for i in range(0, len(s), word_size):
            sub_string = s[i : i + word_size]
            if (
                sub_string in word_map.keys()
                and word_dict[sub_string] < word_map[sub_string]
            ):
                word_dict[sub_string] += 1
                word_count += 1
        return word_count == size

    i = 0
    prev_string = None
    result = []
    for i in range(len(s)):
        sub_string = s[i : i + total_size]
        if prev_string == sub_string or is_substring(sub_string):
            result.append(i)
            prev_string = sub_string
    return result


#### Sliding window - Performant one
def find_substring3(s: str, words: list[str]):
    if not s or not words:
        return []
    wsize = len(words[0])
    size = len(words)
    wlen = len(s)
    word_counter = Counter(words)
    result = []
    for index in range(wsize):
        left = index
        cur_window = Counter()
        counter = 0

        for right in range(left, wlen - wsize + 1, wsize):
            word = s[right: right+wsize]
            if word in word_counter:
                cur_window[word] += 1
                counter += 1
                
                while cur_window[word] > word_counter[word]:
                    left_word = s[left: left + wsize]
                    cur_window[left_word] -= 1
                    counter -= 1
                    left += wsize
                
                if counter == size:
                    result.append(left)
                    left_word = s[left: left + wsize]
                    cur_window[left_word] -= 1
                    counter -= 1
                    left += wsize
            else:
                cur_window.clear()
                counter =0
                left = right + wsize
    return result



if __name__ == "__main__":
    s = "barfoothefoobarman"
    result = find_substring3(s, ["foo", "bar"])
    print(result)
    assert result == [0, 9]


    res = find_substring3(
        "lingmindraboofooowingdingbarrwingmonkeypoundcake",
        ["fooo", "barr", "wing", "ding", "wing"],
    )
    print(res)

    s = "wordgoodgoodgoodbestword"
    result = find_substring3(s, ["word", "good", "best", "good"])
    print(result)
    assert result == [8]

    s = "wordgoodgoodgoodbestword"
    result = find_substring3(s, ["word", "good", "best", "word"])
    print(result)
    assert result == []
