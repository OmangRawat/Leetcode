"""

---> Convert Sorted Array to Binary Search Tree
---> Easy

"""
from tree_func import *


class Solution:
    def sortedArrayToBST(self, nums):
        def dfs(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = Node(nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums) - 1)


in_array = [-10, -3, 0, 5, 9]
a = Solution()
pretty_print(a.sortedArrayToBST(in_array))


"""

Find the mid element make it the root and numbers before it the left and after it the right and continue the same 
process
Reference - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/1363430/Python-Easy-DFS-Clear-explain-Clean-and-Concise
Complexities:
Time -> O(N)
Space -> O(logN)

"""
