"""

---> Maximum Width of Binary Tree
---> Medium

"""

from tree_func import *


class Solution:
    def widthOfBinaryTree(self, root) -> int:
        width = 0
        level = [(1, root)]
        # print([child for child in enumerate((root.left, root.right), 2) if child[1]])
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [child
                     for number, node in level for child in enumerate((node.left, node.right), 2 * number) if child[1]]
            # print([(i[0], i[1].value) for i in level])
        return width


in_array = [1, 3, 2, 5, None, None, 9, 6, None, None, 7]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.widthOfBinaryTree(in_root))

"""

We keep track of leftmost node and the rightmost node in the level in a list and the width of tree till that level is 
the number of the right - left + 1 as we have to include both the numbers too
Reference - https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106650/Python...

"""
