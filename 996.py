"""

---> Number of Squareful Arrays
---> Hard

"""
from collections import Counter


class Solution:
    def numSquarefulPerms(self, nums) -> int:
        def is_square(n):
            if n == 0 or n == 1:
                return True
            if n < 0:
                return False

            x = n // 2

            for i in range(1, x + 1):
                tmp = i * i
                if tmp == n:
                    return True
                elif tmp > n:
                    return False

            return False

        def is_square_dp(n):
            if n not in dp:
                dp[n] = is_square(n)

            return dp[n]

        def dfs(result):
            if len(result) == len(nums):
                ans[0] += 1

            for num in counter:
                prev = result[-1] if len(result) >= 1 else None
                if prev is None or is_square_dp(prev + num):
                    if counter[num] > 0:
                        counter[num] -= 1
                        result.append(num)
                        dfs(result)
                        result.pop()
                        counter[num] += 1

        dp = {}
        ans = [0]
        counter = Counter(nums)
        dfs([])
        return ans[0]


in_nums = [1, 17, 8]
a = Solution()
print(a.numSquarefulPerms(in_nums))
