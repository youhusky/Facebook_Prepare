# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        ans = []
        if self.check(s, wordDict):
            self.dfs(0, len(s), '', s, ans, wordDict)
        return ans
 
    def check(self, s, wordDict):
        dp = [True] + [False] * len(s)
        n = len(s)
        for i in xrange(n):
            for j in xrange(i + 1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[n]
 
    def dfs(self, cur, n, path, s, ans, wordDict):
        if cur == n:
            #print path
            ans.append(path)
            return
 
        for i in xrange(cur, n):
            if s[cur:i + 1] in wordDict and self.check(s[i + 1:n], wordDict):
                if path:
                    self.dfs(i + 1, n, path + ' ' + s[cur:i + 1], s, ans, wordDict)
                else:
                    self.dfs(i + 1, n, s[cur:i + 1], s, ans, wordDict)