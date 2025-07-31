from typing import List

# Given a string s and a dictionary of strings wordDict,
# add spaces in s to construct a sentence where each word
# is a valid dictionary word. Return all such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

def wordBreak( s: str, wordDict: List[str]) -> List[str]:
    dict = set(wordDict)
    return word_break(s, dict)

def word_break(s: str, dict: set):
    size = len(s)
    words = list()
    for i in range(1, size + 1):
        substr = s[:i]
        if substr in dict:
            prefix = substr
            suffix = s[i:size]
            result = word_break(suffix, dict)
            for val in result:
                words.append(prefix + " " + val)
    if s in dict:
        words.append(s)
    return words

if __name__=="__main__":
    result = wordBreak('pineapplepenapple',["apple","pen","applepen","pine","pineapple"])
    print(result)
