"""

---> Add One Row to Tree
---> Medium

"""


from tree_func import *


class Solution:
    def addOneRow(self, root, val: int, depth: int):
        # DFS
        if not root or depth <= 0:
            return None
        if depth == 1:
            return Node(val, root, None)
        if depth == 2:
            root.left = Node(val, root.left, None)
            root.right = Node(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root

    def addOneRow_sol2(self, root, val: int, depth: int):
        # BFS
        dummy, dummy.left = Node(None), root
        row = [dummy]
        for _ in range(depth - 1):
            row = [child for node in row for child in (node.left, node.right) if child]
        for node in row:
            node.left, node.left.left = Node(val), node.left
            node.right, node.right.right = Node(val), node.right
        return dummy.left


in_array = [4, 2, 6, 3, 1, 5]
in_val = 1
in_depth = 2
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print("---> Answer:")
# pretty_print(a.addOneRow(in_root, in_val, in_depth))
pretty_print(a.addOneRow_sol2(in_root, in_val, in_depth))


"""
Reference - https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS

Approach 1:
Do a DFS, 2 cases either it is at depth 1 or 2, decrease depth and go deeper into the tree when the depth is 2 that
means you are on its parent element just add to both children

Complexities:
Time -> O(N)
Space -> O(1)


Approach 2:
Do a BFS, find all the nodes at depth - 1 add val to each of their children

Complexities:
Time -> O(N)
Space -> O(N)

"""