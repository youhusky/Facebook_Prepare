# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# For example:

# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Union find that two node belongs to one root and these two nodes are connected so it is a graph

class Solution(object):
    def validTree(self, n, edges):
        """
        O(N)
        O(N)
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        group = [i for i in range(n)]
        
        for e1,e2 in edges:
            root1 = self.find(e1,group)
            root2 = self.find(e2,group)
            if root1 == root2:
                return False
            else:
                group[root2] = root1
        return len(edges) == n -1
        
    def find(self, e ,group):
        if e == group[e]:
            return e
        else:
            return self.find(group[e], group)
        