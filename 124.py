"""

---> Binary Tree Maximum Path Sum
---> Hard

"""
from tree_func import *


class Solution:
    def maxPathSum(self, root) -> int:
        def dfs(curr_node):
            nonlocal ans
            if curr_node:
                left_sum, right_sum = 0, 0
                if curr_node.left:
                    left_sum = dfs(curr_node.left)
                if curr_node.right:
                    right_sum = dfs(curr_node.right)
                curr_child_sum = max(curr_node.value, curr_node.value + left_sum, curr_node.value + right_sum)
                ans = max(ans, curr_child_sum, curr_node.value + left_sum + right_sum)
                return curr_child_sum
        ans = root.value
        dfs(root)
        return ans


in_array = [-1, -2, 10, -6, None, -3, -6]
# in_array = [-10, 9, 20, None, None, 15, 7]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.maxPathSum(in_root))


"""

Traverse while finding current sum
Paths can be root node + left child or root node + right child or left child + root node + right child

"""
