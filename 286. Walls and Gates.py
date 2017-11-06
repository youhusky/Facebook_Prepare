# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # init
        queue = []
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append((row,col))
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            i,j = queue.pop(0)
            for x,y in direction:
                row = i + x
                col = j + y
                if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and rooms[row][col] == 2147483647:
                    rooms[row][col] = rooms[i][j] + 1
                    queue.append((row, col))
                #print rooms
                    
        
                    