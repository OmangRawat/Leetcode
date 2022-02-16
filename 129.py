"""

---> Sum Root to Leaf Numbers
---> Medium

"""
from tree_func import *
from collections import deque


class Solution:
    def sum_numbers(self, root) -> int:
        # DFS
        def dfs(node, num):
            if not node:
                return 0
            num = num * 10 + node.value
            if not node.left and not node.right:
                return num
            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)

    def sum_numbers_sol2(self, root) -> int:
        # BFS
        dq = deque([(str(root.value), root)])
        ans = 0
        while dq:
            for i in range(len(dq)):
                node_val, curr_node = dq.popleft()

                if not curr_node.left and not curr_node.right:
                    ans += int(node_val)

                else:
                    if curr_node.left:
                        dq.append((node_val + str(curr_node.left.value), curr_node.left))
                    if curr_node.right:
                        dq.append((node_val + str(curr_node.right.value), curr_node.right))
        return ans

    def sum_numbers_sol3(self, root) -> int:
        # Morris Traversal
        tot_sum, cur, depth = 0, 0, 0
        while root:
            if root.left:
                pre, depth = root.left, 1
                while pre.right and pre.right != root:
                    pre, depth = pre.right, depth + 1
                if not pre.right:
                    pre.right = root
                    cur = cur * 10 + root.value
                    root = root.left
                else:
                    pre.right = None
                    if not pre.left:
                        tot_sum += cur
                    cur //= 10 ** depth
                    root = root.right
            else:
                cur = cur * 10 + root.value
                if not root.right:
                    tot_sum += cur
                root = root.right
        return tot_sum


in_array = [1, 2, 3, 4, 5, 6]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.sum_numbers(in_root))
print(a.sum_numbers_sol2(in_root))
print(a.sum_numbers_sol3(in_root))


"""
Reference - https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1556417/C%2B%2BPython-Recursive-and-Iterative-DFS-%2B-BFS-%2B-Morris-Traversal-O(1)-or-Beats-100

Approach 1:
Do a DFS, find net number associated with the leaf nodes then add

Complexities:
Time -> O(N)
Space -> O(Height)

Approach 2:
Do a BFS, keep track of numbers till every level, when you reach leaf node add them to total

Complexities:
Time -> O(N)
Space -> O(N)

Approach 3:
Do a Morris traversal which is used to traverse the tree in O(1) space

Complexities:
Time -> O(N)
Space -> O(1)

"""