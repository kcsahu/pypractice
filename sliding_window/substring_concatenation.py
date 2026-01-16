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


def find_substring1(s: str, words: list[str]):
    if not s or not words:
        return []
    wsize = len(words[0])
    size = len(words)
    word_feq = Counter(words)
    unique_words = len(word_feq)

    def is_substr(word: str) -> bool:
        cur_window = Counter()
        word_counter = 0
        for i in range(0, len(word), wsize):
            sub_str = word[i : i + wsize]
            cur_window[sub_str] += 1
            if sub_str not in word_feq:
                return False
            if cur_window[sub_str] == word_feq[sub_str]:
                word_counter += 1
        return word_counter == unique_words

    result = []
    total_size = size * wsize
    visited = set()
    for i in range(len(s)):
        if s[i : i + wsize] in word_feq:
            sub_str = s[i : i + total_size]
            if sub_str in visited or is_substr(sub_str):
                result.append(i)
                visited.add(sub_str)
    return result


if __name__ == "__main__":
    s = "barfoothefoobarman"
    result = find_substring1(s, ["foo", "bar"])
    print(result)
    assert result == [0, 9]

    s = "wordgoodgoodgoodbestword"
    result = find_substring1(s, ["word","good","best","good"])
    print(result)
    assert result == [8]

    s = 'barfoothefoobarman'
    result = find_substring(s, ["foo","bar"])
    print(result)
    assert result ==[0,9]

    s = "wordgoodgoodgoodbestword"
    result = find_substring(s, ["word","good","best","word"])
    print(result)
    assert result == []
