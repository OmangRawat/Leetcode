"""

---> Step-By-Step Directions From a Binary Tree Node to Another
---> Medium

"""
from tree_func import *


class Solution:
    def getDirections(self, root, startValue, destValue) -> str:
        def lca(curr_node):
            if not curr_node or curr_node.value in (startValue, destValue):
                return curr_node
            left, right = lca(curr_node.left), lca(curr_node.right)
            return curr_node if left and right else left or right

        # root = lca(root)
        pretty_print(root)
        ps = pd = ""
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node.value == startValue:
                ps = path
            if node.value == destValue:
                pd = path
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))
        return "U" * len(ps) + pd


in_array = [5, 1, 2, 3, None, 6, 4]
in_startValue = 3
in_destValue = 6
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.getDirections(in_root, in_startValue, in_destValue))


"""

Get the lowest ancestor common node of start and destination nodes as we need to get the smallest path and don't need 
to check above that, then pass the nodes into stack with the way to reach that from the lca node and make the route till 
source as Us because we need to come to the parent node everytime and add the path from lca to destination node from 
there
Reference - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612179/Python3-lca

"""
