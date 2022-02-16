"""

---> Maximum Product of Two Elements in an Array
---> Easy

"""
from heapq import *


class Solution:
    def maxProduct(self, nums) -> int:
        ele1, ele2 = sorted(nums)[-2:]
        return (ele1 - 1) * (ele2 - 1)

    def maxProduct_sol2(self, nums) -> int:
        heapify(nums)
        ele1, ele2 = nlargest(2, nums)
        return (ele1 - 1) * (ele2 - 1)


in_nums = [1, 5, 4, 5]
a = Solution()
print(a.maxProduct(in_nums))
print(a.maxProduct_sol2(in_nums))


"""
Get the largest 2 nums
Reference- https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/discuss/1496580/Easy-solution-using-heaps-oror-Python3-oror-Heaps
"""
