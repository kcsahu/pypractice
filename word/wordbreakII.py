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
    word_set = set(wordDict)

    def backtrack(s: str)-> list:
        size = len(s)
        words = []
        for i in range(1, size):
            sub_string = s[:i]
            if sub_string in word_set:
                prefix = sub_string
                suffix = s[i:]
                result = backtrack(suffix)
                for word in result:
                    words.append(prefix + ' ' + word)
        if s in word_set:
            words.append(s)
        return words

    return backtrack(s)

if __name__=="__main__":
    result = wordBreak('pineapplepenapple',["apple","pen","applepen","pine","pineapple"])
    print(result)
    assert result.sort() == ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple'].sort()
