# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        O(N)
        O(1)
        :type root: TreeNode
        :rtype: int
        """
        self.best = 1
        self.dfs(root)
        return self.best -1 
    def dfs(self, root):
    	if not root:
    		return 0
    	left = self.dfs(root.left)
    	right = self.dfs(root.right)
    	# include itself
    	self.best = max(self.best, left+right+1)
    	# return either way and plus itself
    	return max(left, right) + 1