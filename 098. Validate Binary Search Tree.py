# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSThelper(root, float("-inf"), float("inf"))
    def isValidBSThelper(self,root,left,right):
        if not root:
            return True
        if left >= root.val or right <= root.val:
            return False
        return self.isValidBSThelper(root.left, left, root.val) and self.isValidBSThelper(root.right, root.val, right)
 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        flag = [True]
        self.check(root, res,flag)
        # print res
        return True if flag[0] else False
    def check(self,root,res,flag):
        if not root:
            return
        self.check(root.left, res,flag)
        if res and root.val <= res[-1]:
            flag[0] = False
            return
        res.append(root.val)   
        self.check(root.right, res, flag)
        
        
        
               
        