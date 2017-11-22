# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum = [float('-inf')]
        self.helper(root, maxSum)
        return maxSum[0]
    def helper(self, root, maxSum):
        if not root:
            return 0
        left = self.helper(root.left, maxSum)
        right = self.helper(root.right, maxSum)
        temp = max(root.val + left, root.val+right, root.val)
        maxSum[0] = max(maxSum[0], temp, root.val+left+right)
        return temp
        