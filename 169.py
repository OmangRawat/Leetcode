"""

---> Majority Element
---> Easy

"""
from collections import Counter


class Solution:
    def majorityElement(self, nums) -> int:
        freq = Counter(nums)
        return max(freq, key=lambda x: freq[x])


in_nums = [2, 2, 1, 1, 1, 2, 2]
a = Solution()
print(a.majorityElement(in_nums))
