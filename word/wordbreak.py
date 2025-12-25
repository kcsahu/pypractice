from typing import List
# * Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
# * space-separated sequence of one or more dictionary words.
# * <p>
# * Note that the same word in the dictionary may be reused multiple times in the segmentation.
# * Input: s = "leetcode", wordDict = ["leet","code"]
# * Output: true
# * Explanation: Return true because "leetcode" can be segmented as "leet code".
# * Input: s = "applepenapple", wordDict = ["apple","pen"]
# * Output: true
# * Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# * Note that you are allowed to reuse a dictionary word.

def wordBreak(s: str, wordDict: List[str]) -> bool:
    dict = set(wordDict)
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for index in range(1, len(s) + 1):
        for j in range(0, index):
            if dp[j] and s[j:index] in dict:
                dp[index] = True
                break
    return dp[len(s)]

def word_break(s: str, wordDict: list[str]) -> bool:
    word_dict = set(wordDict)
    size = len(s)
    dp = [False] * (size + 1)
    dp[0] = True

    def is_present(index):
        for j in range(0, index):
            if dp[j] and s[j:index] in word_dict:
                dp[index] = True
                break

    for i in range(1, size + 1):
        is_present(i)
    return dp[size]





if __name__ == "__main__":
    result = word_break("leetcode", ['leet', 'code'])
    print(result)
    assert result
    result = word_break("catsanddog", ["cats","dog","sand","and","cat"])
    print(result)
    assert result
    result = word_break("catsandog", ["cats","dog","sand","and","cat"])
    print(result)
    assert not result
