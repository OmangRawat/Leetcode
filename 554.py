"""

---> Brick Wall
---> Medium

"""
from collections import defaultdict


class Solution:
    def leastBricks(self, wall) -> int:
        num_of_bricks_at_width = defaultdict(int)

        for row in wall:
            width = 0
            for j in range(len(row) - 1):
                width += row[j]
                num_of_bricks_at_width[width] += 1

        return len(wall) - max(list(num_of_bricks_at_width.values()) + [0])


in_wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
a = Solution()
print(a.leastBricks(in_wall))
