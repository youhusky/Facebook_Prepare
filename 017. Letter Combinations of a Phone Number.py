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
        
    def dfs(self, res, temp, dic,digits,index):
        if len(temp) == len(digits):
            res.append(temp)
            return

        # focus on !
        # digits[index] -> 2: generate a,b,c
        for letter in dic[digits[index]]:
            self.dfs(res, temp+letter, dic, digits, index+1)
            
class Solution2(object):
    def letterCombinations(self, password):
        if not password:
            return []
        res = []
        dic = {'a':"12", 'c':"34"}
        for char in password:
            if char not in dic:
                dic[char] = char
        self.dfs(res, "", dic, password, 0)
        return res
    def dfs(self, res, temp, dic, password, index):
        if index == len(password):
            res.append(temp)
            return 
        for letter in dic[password[index]]:
            self.dfs(res, temp+letter, dic, password, index+1)
m = Solution2()
print m.letterCombinations('abc')
        
