"""

---> Count Complete Tree Nodes
---> Medium

"""


from tree_func import *


class Solution:
    def countNodes(self, root) -> int:
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes_sol2(self, root) -> int:
        def get_depth(curr_root):
            if not curr_root:
                return 0
            # print(curr_root.value)
            # print(curr_root.value, 1 + get_depth(curr_root.left))
            return 1 + get_depth(curr_root.left)

        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)


in_array = [1, 2, 3, 4, 5, 6]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print("Answer -", a.countNodes(in_root))
# print("Answer -", a.countNodes_sol2(in_root))


"""
Approach 1:
Reference - https://leetcode.com/problems/count-complete-tree-nodes/discuss/126600/Python-O(N)-and-O(log(n)-2)-solution-with-explanation

Run through the nodes one at a time

Complexities:
Time -> O(N)
Space -> O(1)

Approach 2:
Either it is left sub tree is full and their is right subtree
Or the complete tree was full till right subtree depth and their are some nodes more on left subtree
Reference - https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
Divide tree in left, right and root

Complexities:
Time -> O(logN * logN)
Space -> 

"""
