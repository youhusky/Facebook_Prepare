class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class DoublyListNode(object):
	def __init__(self, val):	
		self.val = val
		self.next = None
		self.prev = None
					


class Solution(object):
 	"""docstring for Solution"""
 	def __init__(self):
 		
		self.head = None
		self.tail = None

	
	def bstToDoublyList(self,root):
		
		if not root:
			return

		self.bstToDoublyList(root.left)

		node = DoublyListNode(root.val)
		#print node.val,head
		if not self.head:
			self.head = node
			self.tail = node

		else:
			self.tail.next = node
			node.prev = self.tail

			self.tail = node
		#print head.val

		self.bstToDoublyList(root.right)

		return self.head
	
	

test = TreeNode(2)
test.left = TreeNode(1)
test.right = TreeNode(3)
out = Solution()
res = out.bstToDoublyList(test)
print res.val,res.next.val,res.next.next.val
