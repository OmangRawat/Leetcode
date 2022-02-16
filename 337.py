"""

---> House Robber III
---> Medium

"""
from functools import lru_cache

from tree_func import *


class Solution:
    def rob_mine(self, root) -> int:
        @lru_cache(None)
        def dfs(node, parent_robbed):
            if not node:
                return 0
            if parent_robbed:
                # print(node.value, dfs(node.left, False) + dfs(node.right, False))
                return max(dfs(node.left, True), dfs(node.left, False)) + max(dfs(node.right, True),
                                                                       dfs(node.right, False))
            else:
                # print(node.value, node.value + max(dfs(node.left, True), dfs(node.left, False)) +
                #       max(dfs(node.right, True), dfs(node.right, False)))
                return node.value + dfs(node.left, True) + dfs(node.right, True)
        return max(dfs(root, False), dfs(root, True))

    def rob(self, root) -> int:
        @lru_cache(None)
        def dfs(node):
            if not node:
                return 0
            ans = node.value
            if node.left:
                ans += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                ans += dfs(node.right.left) + dfs(node.right.right)
            return max(ans, dfs(node.left) + dfs(node.right))

        return dfs(root)

    def rob_sol2(self, root) -> int:
        def dfs(curr_root):
            if not curr_root:
                return 0, 0
            left = dfs(curr_root.left)
            right = dfs(curr_root.right)
            return curr_root.value + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])

        return max(dfs(root))


in_array = [3, 2, 1, None, 3, None, 4, 10]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.rob_mine(in_root))


"""
Reference - https://leetcode.com/problems/house-robber-iii/discuss/79394/Python-O(n)-code%3A-Optimized-for-Readability

Approach 1:
Use lru cache otherwise TLE
Pass to the children node if their parents have been robbed or not if they have been then they will not be robbed 
otherwise they may or may not be robbed whichever gives better result

Approach 2:
Check for every node if including it will give a better result or contrary and skip a node whenever calculating if the 
node is taken what the best value be 

Approach 3:
Keep track both of if the node is taken what is the best value and if it is not taken what it will be then choose the 
maximum accordingly if the particular node is take the part from their children where there best value when the children 
are not taken ifs calculated otherwise check if taking that node will be beneficial or not on whichever gives maximum 
result

"""
