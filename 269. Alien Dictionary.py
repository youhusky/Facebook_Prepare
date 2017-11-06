# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:
# Given the following words in dictionary,

# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".

# Example 2:
# Given the following words in dictionary,

# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".

# Example 3:
# Given the following words in dictionary,

# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".

# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# Top logical + course schedule ii
# build toplogical graph
class Solution(object):
    def buildgraph(self, word1, word2, indegree, outdegree):
        length = min(len(word1), len(word2))
        for i in range(length):
            if word1[i] != word2[i]:
                if word2[i] not in indegree:
                    indegree[word2[i]] = set()
                if word1[i] not in outdegree:
                    outdegree[word1[i]] = set()
                indegree[word2[i]].add(word1[i])
                outdegree[word1[i]].add(word2[i])
                break 
                
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # queue
        zero_indegree= []
        indegree = {}
        outdegree = {}
        res = []
        
        # init
        nodes = set()
        for word in words:
            for char in word:
                nodes.add(char)
                
        # corner case
        # iterate each word like play and playing
        for i in range(1, len(words)):
            
            if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]:
                continue
            self.buildgraph(words[i-1], words[i],indegree, outdegree)
        # zero indegree
        for node in nodes:
            if node not in indegree:
                zero_indegree.append(node)
                
        # toplogicial
        while zero_indegree:
            prerequest = zero_indegree.pop(0)
            res.append(prerequest)
            if prerequest in outdegree:
                for j in outdegree[prerequest]:
                    indegree[j].remove(prerequest)
                    if not indegree[j]:
                        zero_indegree.append(j)
                del(outdegree[prerequest])
        if outdegree:
            return ""
        return "".join(res)
        
                