"""

---> Find Duplicate Subtrees
---> Medium

"""
from tree_func import *
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root):
        def check(curr_root):
            if not curr_root:
                return "null"
            struct = f"{check(curr_root.left)}, {str(curr_root.value)}, {check(curr_root.right)}"
            nodes[struct].append(curr_root)
            return struct

        nodes = defaultdict(list)
        check(root)
        return [nodes[struct][1] for struct in nodes if len(nodes[struct]) > 1]


in_array = [2, 2, 2, 3, None, 3, None]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
# print(a.findDuplicateSubtrees(in_root))
for i in a.findDuplicateSubtrees(in_root):
    pretty_print(i)


"""

Reference - https://leetcode.com/problems/find-duplicate-subtrees/discuss/106020/Python-easy-understand-solution
Approach 1:
Keep track of each subtree in pre-order or post-order and if the same pattern is their append the root of that subtree 
in te list, if you find any subtree in dict having len more than 1 then their exists a duplicate

Inorder will not work because it gives same ans for any 2 symmetric trees eg. [0, 0, #, #, #] and [0, #, 0, #, #] gives 
#0#0# for both

"""
