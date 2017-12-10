# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution(object):
    result = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = []
        self.search(n, cols)
        return self.result
        
    def search(self, n, cols):
        if len(cols) == n:
            self.result += 1
            return
        
        for col in range(n):
            if not self.isValid(cols, col):
                continue
            self.search(n, cols + [col])

    def isValid(self, cols, col):
        currentRowNumber = len(cols)
        for i in range(currentRowNumber):
            # same column
            if cols[i] == col:
                return False
            # left-top to right-bottom
            if i - cols[i] == currentRowNumber - col:
                return False
            # right-top to left-bottom
            if i + cols[i] == currentRowNumber + col:
                return False
        return True

