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
    ## pre-compute wildcards word
    wsize = len(beginWord)
    wildcard_map = defaultdict(list)
    for w in word_set:
        for i in range(wsize):
            wild_card = w[:i] + '*' + w[i+1:]
            wildcard_map[wild_card].append(w)

    graph = defaultdict(list)
    queue = deque([beginWord])
    visited = {beginWord}
    local_visited = set()
    has_found = False
    while queue and not has_found:
        qsize = len(queue)
        local_visited.clear()
        for i in range(qsize):
            word = queue.pop()
            for j in range(wsize):
                wild_card = word[:j] + '*' + word[j+1:]
                for next_word in wildcard_map.get(wild_card, []):
                    if next_word == word:
                        continue
                    if next_word not in visited:
                        graph[next_word].append(word)
                        if next_word not in local_visited:
                            queue.appendleft(next_word)
                            local_visited.add(next_word)
                    if next_word == endWord:
                        has_found = True
        visited |= local_visited
        # visited = visited.union(local_visited)
    if not has_found:
        return []
    result = []
    path = [endWord]

    def backtrack(word):
        if beginWord == word:
            result.append(path[::-1])
            return
        for next_word in graph[word]:
            path.append(next_word)
            backtrack(next_word)
            path.pop()

    backtrack(endWord)
    return result

if __name__=="__main__":
    res = findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
    print(res)
    assert res.sort() == [['hit', 'hot', 'lot', 'log', 'cog'], ['hit', 'hot', 'dot', 'dog', 'cog']].sort()
    wordList = ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa",
                "ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa",
                "hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa",
                "laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa",
                "obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa",
                "bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba",
                "bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa",
                "bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba",
                "bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba",
                "dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba",
                "gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba",
                "kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba",
                "ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]
    beginWord = 'aaaaa'
    endWord = 'ggggg'
    res = findLadders(beginWord, endWord, wordList)
    print(res)