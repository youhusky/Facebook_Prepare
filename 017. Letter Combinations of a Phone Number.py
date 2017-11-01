# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.



# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# DFS backtracking
class Solution(object):
    def letterCombinations(self, digits):
        """
        O(2^n)
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.dfs(res, '',dic,digits,0)
        return res
        
    def dfs(self, res, temp, dic,digits,num):
        if num == len(digits):
            res.append(temp)
            return

        # focus on !
        for letter in dic[digits[num]]:
            self.dfs(res, temp+letter, dic, digits, num+1)
            
        
        
