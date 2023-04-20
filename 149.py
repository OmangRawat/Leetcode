"""

---> Max Points on a Line
---> Hard

"""
from collections import Counter


class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n == 1:
            return 1

        points.sort()
        ans = 1

        for i in range(n):
            slopes = []

            # from every point get slopes of all other elements to check if they are on same line
            for j in range(i + 1, n):
                if not (points[j][0] - points[i][0]):
                    slopes.append("inf")   # for infinite slope
                else:
                    slopes.append((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]))

            # if slopes > 1 then more than 2 points on a line
            if len(slopes) > 1:
                slope_counter = Counter(slopes)
                max_slope_count = slope_counter.most_common(1)[0][1]
                if max_slope_count > ans:
                    ans = max_slope_count

        return ans + 1


in_points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
a = Solution()
print(a.maxPoints(in_points))
