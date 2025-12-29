#   ##### BFS  ##### Backtracking ####
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of
# words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation
# sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be
# returned as a list of the words [beginWord, s1, s2, ..., sk].
## Example:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
from collections import deque, defaultdict

def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    word_set = set(wordList)
    if endWord not in word_set:
        return []
    dq = deque([beginWord])
    graph = defaultdict(list)
    level = dict()
    level[beginWord] = 0

    while dq:
        next_word = dq.pop()
        cur_level = level[next_word]
        for i in range(len(next_word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                new_word = next_word[:i] + j + next_word[i+1:]
                if new_word in word_set:
                    graph[next_word].append(new_word)
                    if new_word not in level:
                        level[new_word] = cur_level + 1
                        dq.appendleft(new_word)
    if endWord not in level:
        return []
    result = []
    path = [beginWord]

    def backtrack(word: str):
        if word == endWord:
            result.append(path[:])
            return
        for next_word in graph[word]:
            if level[next_word] == level[word] + 1:
                path.append(next_word)
                backtrack(next_word)
                path.pop()

    backtrack(beginWord)
    return result

if __name__=="__main__":
    res = findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
    print(res)
