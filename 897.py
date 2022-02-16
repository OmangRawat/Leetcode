"""

---> Increasing Order Search Tree
---> Easy

"""
from tree_func import *


class Solution:
    def increasingBST(self, root):
        def dfs(node):
            left_start, right_end = node, node

            if node.left:
                left_start, left_end = dfs(node.left)
                left_end.right = node

            if node.right:
                right_start, right_end = dfs(node.right)
                node.right = right_start

            node.left = None
            return left_start, right_end
        return dfs(root)[0]


in_array = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
pretty_print(a.increasingBST(in_root))


"""

Divide every subtre into left and right and get the left end and right end of it bcz left end will be the top and right 
end will connect to root node 
Reference - https://leetcode.com/problems/increasing-order-search-tree/discuss/958059/Python-Inorder-dfs-explained

Complexities:
Time -> 
Space -> 

"""
