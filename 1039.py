"""

---> Minimum Score Triangulation of Polygon
---> Medium

"""


class Solution:
    def minScoreTriangulation(self, values) -> int:
        # Memorization
        final = {}

        def helper(i, j):
            if (i, j) not in final:
                final[(i, j)] = min([(helper(i, k) + helper(k, j) + (values[i] * values[j] * values[k])) for k in range((i + 1), j)] or [0])
            # print(final)
            return final[(i, j)]

        return helper(0, len(values) - 1)

    def minScoreTriangulation_sol2(self, values) -> int:
        # Tabulation
        n = len(values)
        final = [[0] * n for i in range(n)]
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                final[i][j] = min([(final[i][k] + final[k][j] + (values[i] * values[j] * values[k])) for k in range((i + 1), j)])
                # print(final)
        return final[0][n-1]


in_values = [1, 3, 1, 4, 1, 5]
a = Solution()
print(a.minScoreTriangulation(in_values))
# print(a.minScoreTriangulation_sol2(in_values))


"""

When you divide a polygon using a diagonal it divides the polygonal into 2 poly then divide each poly into 2 using 
diagonals until 3 vertices left thus forming triangles
Each poly of n sides can be divided into (n - 2) triangles
Reference - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286705/JavaC%2B%2BPython-DP

Complexities:
Time -> O(N^3)
Space -> O(N^2)

"""