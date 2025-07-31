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


if __name__ == "__main__":
    result = wordBreak("leetcode", ['leet', 'code'])
    print(result)
    result = wordBreak("catsanddog", ["cats","dog","sand","and","cat"])
    print(result)
    result = wordBreak("catsandog", ["cats","dog","sand","and","cat"])
    print(result)
