"""

---> Path Sum II
---> Medium

"""
from tree_func import *


class Solution:
    def pathSum(self, root, targetSum: int):
        def dfs(target, curr_root, curr_path):
            if not curr_root:
                return

            target = target - curr_root.value
            print("Before", curr_path)
            if not curr_root.left and not curr_root.right and target == 0:
                curr_path.append(curr_root.value)
                ans.append(curr_path)
            print("After", curr_path)
            print("After --> ", curr_path + [curr_root.value])
            dfs(target, curr_root.left, curr_path + [curr_root.value])
            dfs(target, curr_root.right, curr_path + [curr_root.value])

            return

        ans = []
        dfs(targetSum, root, curr_path=[])
        return ans


in_array = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
in_target = 22
in_root = to_binary_tree(in_array)
a = Solution()
print(a.pathSum(in_root, in_target))
