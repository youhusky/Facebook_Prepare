class Solution(object):
    def isvalid(self, row, col,rooms):
        if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and rooms[row][col] == 1:
            return True


    def wallsAndGates(self, rooms,start, end):
        """
        O(mn)
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # init
        queue = []
        queue.append([start[0], start[1], 0, ""])
        
        
        visited = [[False for row in range(len(rooms))]for col in range(len(rooms[0]))]
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        res = []
        dist = 0
        while queue:
            i,j,dist,path = queue.pop(0)
            if i == end[0] and j == end[1]:
                return str(dist) + ', path: ' + path 
                
            for x,y in direction:
                row = i + x
                col = j + y
                if self.isvalid(row, col,rooms) and not visited[row][col]:
                    visited[row][col] = True
                    queue.append((row,col,dist+1,path + str(x) + '->'+ str(y) + ','))
                    
        
test = [[1,-1,0,1],[1,1,1,-1],[1,-1,1,-1],[1,-1,1,1]]
start = [0,2]
end = [3,0]
m = Solution().wallsAndGates(test,start, end)
print m           