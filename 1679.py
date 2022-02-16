"""

---> Max Number of K-Sum Pairs
---> Medium

"""
from collections import Counter


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        freq_count = Counter(nums)
        ans = 0
        for num in freq_count.keys():
            ans += min(freq_count[num], freq_count[k - num])
        return ans // 2


in_nums = [1, 2, 3, 4]
in_k = 5
a = Solution()
print(a.maxOperations(in_nums, in_k))
