# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence
# where each word is a valid dictionary word. Return all such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
from sys import prefix
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    word_set = set(wordDict)

    def backtrack(s: str) -> list[str]:
        size = len(s) + 1
        result = []
        for i in range(1, size):
            sub_str = s[:i]
            if sub_str in word_set:
                prefix = sub_str
                suffix = s[i:]
                words = backtrack(suffix)
                for word in words:
                    result.append(prefix + ' ' + word)
        if s in word_set:
            result.append(s)
        return result

    return backtrack(s)

if __name__=="__main__":
    result = wordBreak('pineapplepenapple',["apple","pen","applepen","pine","pineapple"])
    print(result)
    assert result == ["pine apple pen apple","pineapple pen apple","pine applepen apple"]





