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
        dummy = DoublyListNode(0)
        head = dummy
        tail = dummy
        head.next = tail
        tail.prev = head
        leaf = []
        queue = [root]
        while queue:
            level = len(queue)
            while level:
                node = queue.pop(0)
                if not node.left and not node.right:
                    t = DoublyListNode(node.val)
                    temp = tail.prev
                    temp.next = t
                    tail.prev = t
                    t.prev = temp
                    t.next = tail
                    leaf.append(node.val)
                    level -= 1
                    break
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                level -= 1
                
        p = tail.prev
        n = tail.next
        p.next = n
        n.prev = p
        print dummy.next.val
        print dummy.next.next.val
        print dummy.next.next.next.val  
        return leaf
        

m = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
print m.levelOrder(tree) 