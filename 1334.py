"""

---> Find the City With the Smallest Number of Neighbors at a Threshold Distance
---> Medium

"""
from collections import defaultdict
from heapq import *


class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold) -> int:
        # Floyd Warshall
        distance_between_nodes = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    distance_between_nodes[i][j] = 0

        for x in edges:
            distance_between_nodes[x[0]][x[1]] = x[2]
            distance_between_nodes[x[1]][x[0]] = x[2]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance_between_nodes[i][j] = min(distance_between_nodes[i][j], distance_between_nodes[i][k] +
                                                       distance_between_nodes[k][j])

        reachable_cities = {}
        for i in range(n):
            count = 0
            for j in range(n):
                if distance_between_nodes[i][j] <= distanceThreshold and i != j:
                    count += 1
            reachable_cities[i] = count

        smallest_count = float('inf')
        final_city = float('-inf')
        for item in reachable_cities.items():
            if item[1] <= smallest_count and item[0] > final_city:
                smallest_count = item[1]
                final_city = item[0]

        return final_city

    def findTheCity_sol2(self, n: int, edges, distanceThreshold) -> int:
        # Dijkstra
        def dijkstra(start, threshold):
            heap = [(0, start)]
            distance = {node: float('inf') for node in range(n)}
            distance[start] = 0
            visited = set()

            while heap:
                cost, start_city = heappop(heap)

                if start_city in visited:
                    continue

                if cost > threshold:
                    return len(visited) - 1

                visited.add(start_city)

                for end_city in dist_between_nodes[start_city]:
                    new_cost = cost + dist_between_nodes[start_city][end_city]

                    if new_cost < distance[end_city] and end_city not in visited:
                        distance[end_city] = new_cost
                        heappush(heap, (new_cost, end_city))

            return len(visited) - 1

        dist_between_nodes = defaultdict(dict)

        for city1, city2, weight in edges:
            dist_between_nodes[city1][city2] = weight
            dist_between_nodes[city2][city1] = weight

        ans = (-1, n)

        for i in range(n):
            connected_cities = dijkstra(i, distanceThreshold)
            if connected_cities < ans[1] or (connected_cities == ans[1] and i > ans[0]):
                ans = (i, connected_cities)
        return ans[0]


in_n = 5
in_edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
in_threshold = 2
a = Solution()
print(a.findTheCity(in_n, in_edges, in_threshold))
print(a.findTheCity_sol2(in_n, in_edges, in_threshold))


"""
Approach 1:
Floyd Warshall
Make a matrix and fill up all data about distance between 2 nodes then compare if the distance is smaller than threshold 
+1 to the number of neighbors it has. Find the node with smallest number of neighbors and the largest city among them

Reference - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/1601926/All-Pair-Shortest-Path-(Floyd-Warshall)-Python-3
 
Complexities:
Time -> O(N^3)
Space -> O(n^2)


Approach 2:
Dijkstra
Find no. of neighbors less than threshold between 2 nodes then use to find same for start to next node 

Reference - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/1485218/Python-Dijkstra-solution-beats-97

Complexities:
Time -> 
Space -> 
 
"""
