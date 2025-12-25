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

def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_dict = set(wordDict)
    size = len(s)
    dp = [False] * (size + 1)
    dp[0] = True
    def backtrack(index: int):
        for j in range(0, index):
            if dp[j] and s[j:index] in word_dict:
                dp[index] = True
                break
    for i in range(1, size + 1):
        backtrack(i)
    return dp[-1]

if __name__ == "__main__":
    result = wordBreak("leetcode", ['leet', 'code'])
    print(result)
    assert result
    result = wordBreak("catsanddog", ["cats","dog","sand","and","cat"])
    print(result)
    assert result
    result = wordBreak("catsandog", ["cats","dog","sand","and","cat"])
    print(result)
    assert not result