# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# Definition for a binary tree node.
class DoublyListNode(object):
    def __init__(self, val):    
        self.val = val
        self.next = None
        self.prev = None
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return None
        res = [[root.val]]
        queue = [root]
        while queue:
            level = len(queue)
            temp = []
            while level:
                node = queue.pop(0)
                if not node.left:
                    temp.append(".")
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if not node.right:
                    temp.append(".")
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
                level -= 1
            res.append(list(temp)) # diff temp

        return res[:-1]

m = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
print m.levelOrder(tree) 