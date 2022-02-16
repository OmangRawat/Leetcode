"""

---> Maximum Number of Points with Cost
---> Medium

"""


class Solution:
    def maxPoints(self, points) -> int:
        m, n = len(points), len(points[0])
        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)
            for j in range(n):
                points[i][j] = max(points[i][j], points[i][j - 1] - 1 if j else 0)
                points[i + 1][j] += points[i][j]
        return max(points[-1])


in_points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
a = Solution()
print(a.maxPoints(in_points))


"""

Reference - https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1345059/Python-DP-like-Solution

Complexities:
Time -> O(N*M)
Space -> O(1)

"""
