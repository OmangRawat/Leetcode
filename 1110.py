"""

---> Delete Nodes And Return Forest
---> Medium

"""
from tree_func import *


class Solution:
    def delNodes(self, root, to_delete):
        # to_delete = set(to_delete)
        ans = []

        def dfs(in_root, parent_exist):
            if in_root is None:
                return None
            if in_root.value in to_delete:
                in_root.left = dfs(in_root.left, False)
                in_root.right = dfs(in_root.right, False)
                return None
            else:
                if not parent_exist:
                    ans.append(in_root)
                in_root.left = dfs(in_root.left, True)
                in_root.right = dfs(in_root.right, True)
                return in_root

        dfs(root, False)
        return ans


in_array = [1, 2, 3, 4, 5, 6, 7]
in_delete = [3, 5]
in_tree = to_binary_tree(in_array)
pretty_print(in_tree)
a = Solution()
for i in a.delNodes(in_tree, in_delete):
    pretty_print(i)


"""

We need to pass to children if their parent still exists if it isn't that means it will be a different tree and tell 
the parents if their child still exist or return None
Reference - https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328854/Python-Recursion-with-explanation-Question-seen-in-a-2016-interview

"""
