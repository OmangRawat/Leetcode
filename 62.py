"""

---> Unique Paths
---> Medium

"""
from itertools import product
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

    def uniquePaths_sol1(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


in_m = 3
in_n = 7
a = Solution()
print(a.uniquePaths(in_m, in_n))
