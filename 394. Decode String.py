# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

# use stack to save prev string and prev number
class Solution(object):
    def decodeString(self, s):
        """
        O(N)
        O(N)
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        res = []
        stack = []
        curnum = 0
        curstring = ""
        for char in s:
            if char.isdigit():
                curnum = curnum*10 + int(char)
            elif char == '[':
                stack.append(curnum)
                stack.append(curstring)
                curstring = ""
                curnum = 0
            elif char == ']':
                prevstring = stack.pop()
                prenumber = stack.pop()
                curstring = prevstring+prenumber*curstring
            else:
                curstring += char
        return curstring
                
            
