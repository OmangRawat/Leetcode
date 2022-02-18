"""

---> Majority Element II
---> Medium

"""
from collections import Counter


class Solution:
    def majorityElement(self, nums):
        freq = Counter(nums)
        ans = [x for x in freq if freq[x] > len(nums)/3]
        return ans


in_nums = [3, 2, 3]
a = Solution()
print(a.majorityElement(in_nums))
