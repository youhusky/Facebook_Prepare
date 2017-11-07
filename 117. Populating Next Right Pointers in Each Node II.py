# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:

# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, node):
        tail = dummy = TreeLinkNode(0)
        while node:
            
            # check left
            tail.next = node.left
            if tail.next:
                tail = tail.next
                
            # check right
            tail.next = node.right
            if tail.next:
                tail = tail.next
            # check level move from left to right one 
            node = node.next
            if not node:
                tail = dummy
                # move from dummy to node.left if point to the leaf node 
                # then dummy.next == None break loop
                node = dummy.next
