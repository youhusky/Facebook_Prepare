class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.children = []


def findLCA(root,p,q):
    
    if root.val == p or root.val == q:
        return root

    count = 0
    temp = None

    # corner case left node or without p,q return  None
    for child in root.children:
        
        res = findLCA(child, p, q)
        # if find one return root
        if res:
            count += 1
            temp = res
            
    if count == 2:
        return root
    return temp


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
print findLCA(n1,4,5).val