"""

---> Construct Binary Tree from Preorder and Inorder Traversal
---> Medium

"""
from tree_func import *


class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            node = Node(preorder[0])
            preorder.remove(node.value)
            limit = inorder.index(node.value)
            node.left = self.buildTree(preorder, inorder[:limit])
            node.right = self.buildTree(preorder, inorder[limit + 1:])
            return node


in_pre = [3, 9, 20, 15, 7]
in_in = [9, 3, 15, 20, 7]
a = Solution()
pretty_print(a.buildTree(in_pre, in_in))
