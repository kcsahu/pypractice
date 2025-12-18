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
import heapq


def find_substring(s: str, words: list):
    size, word_size = len(words), len(words[0])
    total_size = word_size * size
    word_map = {}
    for word in words:
        word_count = word_map.get(word, 0)
        word_map[word] = word_count + 1
    def is_substring(s: str)-> bool:
        word_dict = {}
        for i in range(0, len(s), word_size):
            sub_string = s[i: i + word_size]
            if sub_string in word_map.keys():
                word_count = word_dict.get(sub_string, 0)
                word_dict[sub_string] = word_count + 1
        return word_map == word_dict

    i = 0
    prev_string = None
    result = []
    for i in range(len(s)):
        sub_string = s[i:i+total_size]
        if prev_string == sub_string or is_substring(sub_string):
            result.append(i)
            prev_string = sub_string
    return result



if __name__ == "__main__":
    s = 'barfoothefoobarman'
    result = find_substring(s, ["foo","bar"])
    print(result)
    assert result ==[0,9]

    s = "wordgoodgoodgoodbestword"
    result = find_substring(s, ["word","good","best","word"])
    print(result)
    assert result == []
