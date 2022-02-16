"""

---> Jump Game VI
---> Medium

"""
from collections import deque


class Solution:
    def maxResult(self, nums, k: int) -> int:
        ans = nums[0]
        d = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            ans = nums[i] + d[0][0]
            while d and d[-1][0] < ans:
                d.pop()
            d.append((ans, i))

            if i - k == d[0][1]:
                # print("....")
                d.popleft()
            # print(dp, d)
        return ans


in_nums = [1, -5, -20, 4, -1, 3, -6, -3]
in_k = 2
a = Solution()
print(a.maxResult(in_nums, in_k))


"""
Keep track of sum till last number and at max last k steps in queue
Reference - https://leetcode.com/problems/jump-game-vi/discuss/978497/Python-DP-%2B-Sliding-Window-Maximum-problem-combined

Complexities:
Time -> O(N*K)
Space -> O(N)

"""
