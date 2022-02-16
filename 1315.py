"""

---> Sum of Nodes with Even-Valued Grandparent
---> Medium

"""


from tree_func import *


class Solution:
    def sumEvenGrandparent(self, root) -> int:
        # DFS
        def dfs(node, parent, g_parent):
            if not node:
                return
            nonlocal ans
            if parent and g_parent and g_parent.value % 2 == 0:
                ans += node.value
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        ans = 0
        dfs(root, None, None)
        return ans


in_array = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.sumEvenGrandparent(in_root))


"""

Keep track of grandparent and parent of a node, update accordingly

DFS
Reference - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/480981/Simple-Python-3-DFS-solution-beats-99.38

"""
