"""

---> Maximum Level Sum of a Binary Tree
---> Medium

"""
from tree_func import *


class Solution:
    def maxLevelSum(self, root) -> int:
        # DFS
        def dfs(node, level: int) -> None:
            if not node:
                return
            if len(node_list) == level:
                node_list.append(node.value)
            else:
                node_list[level] += node.value
            print(node_list)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        node_list = []
        dfs(root, 0)
        return 1 + node_list.index(max(node_list))

    def maxLevelSum_sol2(self, root) -> int:
        # BFS
        max_sum, level, max_level = -float('inf'), 0, 0
        q = deque()
        q.append(root)

        while q:
            level += 1
            sum_of_level = 0

            for _ in range(len(q)):
                node = q.popleft()
                sum_of_level += node.value

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if max_sum < sum_of_level:
                max_sum, max_level = sum_of_level, level
        return max_level


# in_array = [989, None, 10250, 98693, -89388, None, None, None, -32127]
in_array = [1, 7, 0, 7, -8, None, None]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
# print(a.maxLevelSum(in_root))
print(a.maxLevelSum_sol2(in_root))


"""

Approach 1:
Make a list keeping track of sum of each level

Approach 2:
Keep track of max_sum and its level and update if any levl gets a bigger sum

Reference - https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/discuss/360968/JavaPython-3-Two-codes-language%3A-BFS-level-traversal-and-DFS-level-sum.

Complexities:
Time -> O(N)
Space -> O(N)

"""
