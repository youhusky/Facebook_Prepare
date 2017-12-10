# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n <= 0:
            return result

        cols = []
        self.search(n, cols, result);
        return result
        
    def search(self, n, cols, result):
        if len(cols) == n:
            result.append(self.drawBoard(cols))
            return
        
        for col in range(n):
            if not self.isValid(cols, col):
                continue
            cols.append(col)
            #print cols
            self.search(n, cols , result)
            cols.pop()
            
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
        
    def drawBoard(self, cols):
        board = []
        for i in range(len(cols)):
            line = ""
            for j in range(len(cols)):
                if j == cols[i]:
                    line += "Q"
                else:
                    line += "."
            board.append(line)
        return board

