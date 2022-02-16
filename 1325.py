"""

---> Delete Leaves With a Given Value
---> Medium

"""
from tree_func import *


class Solution:
    def removeLeafNodes(self, root, target: int):
        if not root:
            return None
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.value == target:
            return None
        else:
            return root


in_array = [1, 2, 3, 2, None, 2, 4]
in_target = 2
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
pretty_print(a.removeLeafNodes(in_root, in_target))


"""

Traverse in DFS and check for leaf node and given value equal it to none else return root
Reference - https://leetcode.com/problems/delete-leaves-with-a-given-value/discuss/484264/JavaC%2B%2BPython-Recursion-Solution

"""
