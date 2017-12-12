# To remove only spaces use str.replace:

# sentence = sentence.replace(' ', '')
# To remove all whitespace characters (space, tab, newline, and so on) you can use split then join:

# sentence = ''.join(sentence.split())
# Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or char != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
            