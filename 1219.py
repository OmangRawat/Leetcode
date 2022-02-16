"""

---> Path with Maximum Gold
---> Medium

"""


class Solution:
    def getMaximumGold(self, grid) -> int:
        grid_rows, grid_columns = len(grid), len(grid[0])

        def valid(x, y):
            return 0 <= x < grid_rows and 0 <= y < grid_columns

        def dfs(x, y):
            stack = [(x, y, grid[x][y], {(x, y)})]
            ans = 0
            while stack:
                curr_x, curr_y, curr_total_gold, visited = stack.pop()
                ans = max(ans, curr_total_gold)
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    next_x, next_y = curr_x + dx, curr_y + dy
                    if valid(next_x, next_y) and (next_x, next_y) not in visited and grid[next_x][next_y] != 0:
                        stack.append((next_x, next_y, curr_total_gold + grid[next_x][next_y], visited | {(next_x, next_y)}))

            return ans

        max_gold = 0
        for i in range(grid_rows):
            for j in range(grid_columns):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold


in_grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
a = Solution()
print(a.getMaximumGold(in_grid))
