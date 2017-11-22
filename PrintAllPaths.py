class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.children = []

class Result(object):
    def __init__(self, node, maxDepth):
        self.node = node
        self.maxDepth = maxDepth

def helper(root):
    # corner case
    if not root.children:
        return Result(root,1)
    size = len(root.children)
    maxDepth = float('-inf')

    temp = Result(root, maxDepth)
    for i in range(size):
        child = helper(root.children[i])
        # find more deep node
        if child.maxDepth > maxDepth:
            maxDepth = child.maxDepth
            temp.node = child.node
            temp.maxDepth = child.maxDepth+1
        # same depth
        elif child.maxDepth == maxDepth:
            temp.node = root
    return temp

def find(root):
    if not root or not root.children:
        return root
    return helper(root).node

# 1
# /\\
# 2,3,4
# /\
# 5,6
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.children = [n2, n3,n4]
n5 = TreeNode(5)
n6 = TreeNode(6)
n2.children =[n5,n6]

print find(n1).val