# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# For example, you may serialize the following tree

#     1
#    / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Credits:
# Special thanks to @Louis1992 for adding this problem and creating all test cases.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

	# Level order Traverse empty is equals to '#' 
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
            res.append(str(node.val) if node else "#")
        # -3 -> str -3#
        # 3,1,2,'#','#','#','#'
        return ",".join(res).strip(',')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = []
        for i in data.split(','):
            if i != '#':
                nodes.append(TreeNode(int(i)))
            else:
                nodes.append(None)
        queue = [nodes[0]]
        index = 1
        while queue:
            node = queue.pop(0)
            if index < len(nodes) and nodes[index]:
                node.left = nodes[index]
                queue.append(nodes[index])
            if index+1 < len(nodes) and nodes[index+1]:
                node.right = nodes[index+1]
                queue.append(nodes[index+1])
            index += 2
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))