"""

---> Univalued Binary Tree
---> Easy

"""


from tree_func import *


class Solution:
    def isUnivalTree(self, root) -> bool:
        def dfs(node):
            # pretty_print(node)
            # print(node is None or node.value == root.value and dfs(node.left) and dfs(node.right))
            return node is None or node.value == root.value and dfs(node.left) and dfs(node.right)
        return dfs(root)


in_array = [1, 1, 1, 1, 1, None, 1]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print("Answer -", a.isUnivalTree(in_root))
# print("Answer -", a.isUnivalTree(in_root))


"""
Check if node is none or node.value should be equal to root value for that and every other node in its children
Reference - https://leetcode.com/problems/univalued-binary-tree/discuss/211397/JavaPython-3-BFS-and-DFS-clean-codes-w-brief-analysis.
"""
