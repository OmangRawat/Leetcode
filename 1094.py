"""

---> Car Pooling
---> Medium

"""
from heapq import *


class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        heap = []

        for (c, f, t) in trips:
            print(heap)
            while heap and heap[0][0] <= f:
                v = heappop(heap)[1]
                capacity += v
            if c > capacity:
                return False
            else:
                capacity -= c
                heappush(heap, (t, c))

        return True

    def carPooling_sol2(self, trips, capacity: int) -> bool:
        all_trips = []
        for trip in trips:
            all_trips.append((trip[1], trip[0]))
            all_trips.append((trip[2], -trip[0]))
        all_trips.sort()

        count = 0
        for i in all_trips:
            count += i[1]
            if count > capacity:
                return False
        return True


in_trips = [[2, 1, 5], [3, 3, 7]]
in_capacity = 5
a = Solution()
print(a.carPooling(in_trips, in_capacity))
# print(a.carPooling_sol2(in_trips, in_capacity))


"""

Approach 1:
Add to heap one by one from the array sorted using the pickup point and decrease the capacity of the car, check for the 
last entered location's end point to next pickups start point if comes before restore the capacity of the car, If anyone 
of the trips mismatch it is a false

Approach 2:
Divide each trip into start point and capacity and end point and -1*capacity, sort them now check for the capacity for 
each trip

Reference - https://leetcode.com/problems/car-pooling/discuss/1596704/Python-Min-Heap

"""
