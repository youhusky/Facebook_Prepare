# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# Note: If the given node has no in-order successor in the tree, return null.

class Solution(object):
	def inorderSuccessor(self, root,p):
		succ = None
		while root:
			if p.val < root.val:
				succ = root
				root = root.left
			else:
				root = root.right
		return succ


# follow up
	def inorderPrevsessor(self, root, p):
		prev = None
		while root:
			if p.val < root.val:
				root = root.left
			else:
				prev = root
				root = root.right
		return prev