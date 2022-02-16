"""

---> Path Sum III
---> Medium

"""
from tree_func import *


class Solution:
    def pathSum(self, root, targetSum) -> int:
        def check(node, target_left):
            if node is None:
                return

            nonlocal ans
            if node.value == target_left:
                # print(node.value)
                ans += 1

            check(node.left, target_left - node.value)
            check(node.right, target_left - node.value)

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            check(node, targetSum)
            dfs(node.right)

        ans = 0
        dfs(root)
        return ans


# in_array = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
in_array = [1, None, 2, None, 3, None, 4, None, 5]
in_target = 3
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.pathSum(in_root, in_target))


"""

Check for every node as the start point if the target sum can be achieved, by decreasing the node value of the current 
node and finding nodes that will add up to the remaning sem in its subtree
Reference - https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

Complexities:
Time -> O(N^2) for one sided tree, O(NlogN) for balanced tree
Space -> O(1)

"""
