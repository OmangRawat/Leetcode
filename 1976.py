"""

---> Number of Ways to Arrive at Destination
---> Medium

"""
import math
from collections import defaultdict
from heapq import *


class Solution:
    def countPaths(self, n: int, roads) -> int:
        road_graph = defaultdict(list)

        for u, v, t in roads:
            road_graph[u].append((v, t))
            road_graph[v].append((u, t))

        times, path = [math.inf] * n, [0] * n
        path[0] = 1

        pq = [(0, 0)]

        while pq:
            tu, u = heappop(pq)

            for v, t_uv in road_graph[u]:
                if times[v] == (new_time := tu + t_uv):
                    path[v] = (path[v] + path[u]) % (10 ** 9 + 7)
                elif times[v] > new_time:
                    path[v] = path[u]
                    times[v] = new_time
                    heappush(pq, (new_time, v))

        return path[-1]


in_n = 7
in_roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
a = Solution()
print(a.countPaths(in_n, in_roads))


"""
Dijkstra
Reference - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/discuss/1620878/Python-Simple-Min-Heap-Impl

Complexities:
Time -> O(R + NlogN)
Space -> O(R + N)

"""
