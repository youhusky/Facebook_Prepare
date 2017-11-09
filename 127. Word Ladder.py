# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Bi -BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        O(NL)
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not beginWord or not endWord or not wordList:
            return 0
        if endWord not in wordList:
            return 0
        count = 0

        wordList = set(wordList)

        
        ## Bi-way begin always small
        beginSet = set()
        endSet = set()

        beginSet.add(beginWord)
        endSet.add(endWord)
        while beginSet and endSet:
            count += 1
            # change two set
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            nextSet = set()
            for each_word in beginSet:
                for char in range(len(each_word)):
                    for i in range(26):
                        # not the same word
                        if chr(97+i) != each_word[char]:
                            new_word = each_word[:char] + chr(97+i) + each_word[char+1:]
                            if new_word in wordList:
                                wordList.remove(new_word)
                                nextSet.add(new_word)
                            if new_word in endSet:
                                return count + 1
            beginSet = nextSet
        return 0
                    
            
        
        
        
