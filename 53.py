"""

---> Maximum Subarray
---> Easy

"""
import math


class Solution:
    def max_sub_array(self, nums):
        net, ans = 0, -1*math.inf
        for i in nums:
            net = max(i, net + i)
            ans = max(ans, net)
        return ans


in_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = Solution()
print(a.max_sub_array(in_nums))

"""
Kadane's Algo

Complexities:
Time ->  O(N)
Space -> O(1)

"""

