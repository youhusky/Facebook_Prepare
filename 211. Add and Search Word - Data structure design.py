# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.

# pass version need to focus on the init Trie dict get function
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.node = defaultdict()
        self.isWord = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for letter in word:
            child = curr.node.get(letter)
            if child is None:
                child = TrieNode()
                curr.node[letter] = child
            curr = child
        curr.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)
    
    def find(self, trie, word):
        if word == '':
            return trie.isWord
        
        if word[0] == '.':
            for i in trie.node:
                if self.find(trie.node[i], word[1:]):
                    return True
        else:
            child = trie.node.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# my old way which MLE

from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.node = defaultdict(TrieNode)
        self.isWord = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            curr = curr.node[char]
        curr.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)
    
    def find(self, trie, word):
        if word == '':
            return trie.isWord
        
        if word[0] == '.':
            for i in trie.node:
                if self.find(trie.node[i], word[1:]):
                    return True
        else:
            child = trie.node[word[0]]
            
            return self.find(child, word[1:])
        return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)