"""

---> Merge Two Binary Trees
---> Easy

"""
from tree_func import *


class Solution:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            root = Node(root1.value + root2.value)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2


in_array1 = [1, 3, 2, 5]
in_array2 = [2, 1, 3, None, 4, None, 7]
in_tree1 = to_binary_tree(in_array1)
in_tree2 = to_binary_tree(in_array2)
pretty_print(in_tree1)
pretty_print(in_tree2)
a = Solution()
pretty_print(a.mergeTrees(in_tree1, in_tree2))


"""

For the position where both trees have elements sum them and add node else the tree whichever has the node will be 
returned
Reference - https://leetcode.com/problems/merge-two-binary-trees/discuss/104301/Short-Recursive-Solution-w-Python-and-C%2B%2B
"""
