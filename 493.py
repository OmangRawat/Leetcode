"""

---> Reverse Pairs
---> Hard

"""
from bisect import bisect_right, insort


class Solution:
    def reversePairs(self, nums) -> int:
        num_arr = []
        ans = 0

        for i in nums:
            ans += len(num_arr) - bisect_right(num_arr, 2 * i)
            insort(num_arr, i)

        return ans
    
    
in_nums = [1, 3, 2, 3, 1]
a = Solution()
print(a.reversePairs(in_nums))
