"""

---> Path With Minimum Effort
---> Medium

"""
from heapq import *


class Solution:
    def minimumEffortPath(self, heights) -> int:
        # Dijkstra's Algorithm with heap
        n, m = len(heights), len(heights[0])
        heap, ans = [(0, 0, 0)], 0
        points_seen = set()

        while heap:
            effort, row, column = heappop(heap)
            ans = max(effort, ans)
            points_seen.add((row, column))

            if row == n - 1 and column == m - 1:
                return ans

            for next_row, next_column in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)):
                if 0 <= next_row < n and 0 <= next_column < m and (next_row, next_column) not in points_seen:
                    heappush(heap, (abs(heights[next_row][next_column] - heights[row][column]), next_row, next_column))
            # print(heap)


in_heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
a = Solution()
print(a.minimumEffortPath(in_heights))


"""

Approach 1:
Put all the elements according to one step up, down, left and right. Pop out the one which has the minimum effort and 
take max of the popped one and ans
If you reach the end node return ans

Reference - https://leetcode.com/problems/path-with-minimum-effort/discuss/1631924/python-bfs-with-heap

"""
