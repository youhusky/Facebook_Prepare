# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.
# Solution 1 sorted str
class Solution(object):
    def groupAnagrams(self, strs):
        """
        O(nklgk)
        k-length of word in list
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            ori = word
            # imp
            word = str(sorted(word))
            
            if word not in dic:
                dic[word] = [ori]
            else:
                dic[word].append(ori)
        return dic.values()

# Note: All inputs will be in lower-case.
# Solution 2

# we can create size equals to 26 list to store

class Solution(object):
    def groupAnagrams(self, strs):
        """
        O(nk)
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        dic = {}
        
        for word in strs:
            # init count
            count = [0 for _ in range(26)]
            for char in word:
                count[ord(char) - ord('a')] += 1
                
            # rebuild str  
            temp = ""
            for i in range(26):
                if count[i] != 0:
                    temp += chr(i+97) * count[i]
            #print temp
            if temp not in dic:
                dic[temp] = [word]
            else:
                dic[temp].append(word)
        return dic.values()

        