"""

---> Unique Paths III
---> Hard

"""


class Solution:
    def uniquePathsIII(self, grid):
        def move_next(step, x, y):
            ans = 0
            for y_cord, x_cord in directions:
                next_x, next_y = x + y_cord, y + x_cord

                if n > next_y >= 0 <= next_x < m:
                    if grid[next_x][next_y] == 0:
                        grid[next_x][next_y] = -1
                        ans += move_next(step + 1, next_x, next_y)
                        grid[next_x][next_y] = 0

                    if grid[next_x][next_y] == 2 and step == cell:
                        ans += 1
            return ans

        m, n = len(grid), len(grid[0])
        start, cell = [0, 0], 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = [i, j]
                if grid[i][j] == 0:
                    cell += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        return move_next(0, start[0], start[1])


in_grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
a = Solution()
print(a.uniquePathsIII(in_grid))


"""
Reference - https://leetcode.com/problems/unique-paths-iii/discuss/1554970/DFS-with-python-beats-100-in-time
"""
