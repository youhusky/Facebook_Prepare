class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class DoublyListNode(object):
    def __init__(self, val):    
        self.val = val
        self.next = None
        self.prev = None
class Solution2(object):
    def binaryTreePaths(self, root,node):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        self.helper(root, res, str(root.val),node)
        dummy = DoublyListNode(0)
        head = dummy
        tail = dummy
        head.next = tail
        tail.prev = head
        for i in res[0]:
            t = DoublyListNode(int(i))
            temp = tail.prev
            temp.next = t
            tail.prev = t
            t.prev = temp
            t.next = tail
        # delete dummy
        p = tail.prev
        n = tail.next
        p.next = n
        n.prev = p
        print dummy.next.val
        print dummy.next.next.val
        print dummy.next.next.next.val
        return res
    def helper(self, root, res, temp,node):
        if not root:
            return 
        if root.val==node.val:
            res.append(list(temp))
            return 
        if root.val>node.val:
            if root.left:
                self.helper(root.left, res, temp + str(root.left.val),node)
        else:
            if root.right:
                self.helper(root.right, res , temp +str(root.right.val),node)

m = Solution2()
tree = TreeNode(5)
tree.left = TreeNode(1)
tree.right = TreeNode(6)
tree.right.left = TreeNode(4)
print m.binaryTreePaths(tree,TreeNode(1))