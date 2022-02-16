"""

---> Maximize Score After N Operations
---> Hard

"""
import math
from math import gcd


class Solution:
    def maxScore(self, nums) -> int:
        def dfs(operation):
            if operation == 0:
                dp[operation] = 0
                return 0
            if operation in dp:
                return dp[operation]

            best_score = - math.inf
            kth = 1 + n // 2 - sum([1 for i in range(n) if operation & 1 << i]) // 2
            for i in range(n):
                for j in range(i + 1, n):
                    if operation & 1 << i and operation & 1 << j:
                        score = kth * gcd(nums[i], nums[j])
                        best_score = max(best_score, score + dfs(operation ^ (1 << i) ^ (1 << j)))
            dp[operation] = best_score
            return best_score

        dp = {}
        n = len(nums)
        return dfs(2 ** len(nums) - 1)


in_nums = [1, 2]
a = Solution()
print(a.maxScore(in_nums))


"""
Reference - https://leetcode.com/problems/maximize-score-after-n-operations/discuss/1563308/Python-Bitmasking-%2B-DP
"""
