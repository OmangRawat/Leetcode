"""

---> Minimum Number of Refueling Stops
---> Hard

"""
from collections import defaultdict
from heapq import *


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        heap = [-startFuel]
        step = -1
        index = 0
        max_dist_reachable = 0
        while heap:
            max_dist_reachable += -heappop(heap)
            step += 1
            if max_dist_reachable >= target:
                return step
            while index < len(stations) and stations[index][0] <= max_dist_reachable:
                heappush(heap, -stations[index][1])
                index += 1
        return -1

    def minRefuelStops_sol2(self, target: int, startFuel: int, stations) -> int:
        dp = defaultdict(int)
        dp[0], n = startFuel, len(stations)

        for i in range(n):
            pos, fuel = stations[i]

            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)

        for i in range(n + 1):
            if dp[i] >= target:
                return i

        return -1


in_target = 100
in_startFuel = 10
in_stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
a = Solution()
print(a.minRefuelStops(in_target, in_startFuel, in_stations))
print(a.minRefuelStops_sol2(in_target, in_startFuel, in_stations))


"""

Approach 1:
Keep track of max distance reachable from the petrol pump in reach. Put the ones in reach in a heap and take the one 
with maximum petrol untl you reach the final destination
Reference - https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/1590224/Python3-heap-solution-with-time-O(nlogn)-and-space-O(n)

Approach 2:
Using dynamic programming, keep track of the max dist the car can go using 0 to len(stations), The distance is the max 
of the distance he can travel using k - 1 pumps + the fuel in kth pump, Return the number of pumps that gives the 
distance greater than or equal to the target
Reference - https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/1561848/Simple-Python-Solution-or-DP-8-Lines-or-O(n**2)

"""
