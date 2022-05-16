"""

---> Swim in Rising Water
---> Hard

"""
from heapq import heappush, heappop


class Solution:
    def swimInWater(self, grid) -> int:
        def is_valid(x, y):
            return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

        def traverse(i, j):
            for a, b in moves:
                new_i, new_j = i + a, j + b
                if is_valid(new_i, new_j) and (new_i, new_j) not in visited:
                    heappush(heap, (grid[new_i][new_j], new_i, new_j))
                    visited.add((new_i, new_j))

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        ans = 0
        while len(heap):
            # print(heap)
            curr_ele, curr_i, curr_j = heappop(heap)
            ans = max(ans, curr_ele)
            if curr_i == len(grid[0]) - 1 and curr_j == len(grid) - 1:
                return ans
            traverse(curr_i, curr_j)


in_grid = [[0, 2], [1, 3]]
# in_grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
a = Solution()
print(a.swimInWater(in_grid))
