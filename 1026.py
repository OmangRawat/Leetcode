"""

---> Maximum Difference Between Node and Ancestor
---> Medium

"""

from tree_func import *


class Solution:
    def maxAncestorDiff(self, root) -> int:
        ans = 0

        def dfs(node, low, high):
            if not node:
                return
            nonlocal ans
            ans = max(ans, abs(node.value - low), abs(node.value - high))
            low1, high1 = min(low, node.value), max(high, node.value)
            dfs(node.left, low1, high1)
            dfs(node.right, low1, high1)

        dfs(root, root.value, root.value)
        return ans


in_array = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.maxAncestorDiff(in_root))


"""

We keep track of min and max elements and max difference then for every node check if you get a lower difference
Reference - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/929284/Python-O(n)%3A-look-at-child-explained

"""
