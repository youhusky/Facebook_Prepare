# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isBalanced(self, root):
        """
        O(n)
        O(1)
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root) != -1
    def check(self, root):
    	if not root:
    		return 0

    	left = self.check(root.left)
    	right = self.check(root.right)
    	if left == -1 or right == -1 or abs(left-right)>1:
    		return -1
    	return max(left, right) +1