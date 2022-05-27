"""

---> Cheapest Flights Within K Stops
---> Medium

"""
from collections import defaultdict
from heapq import *


class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        ad_dict = defaultdict(list)
        ends = set()
        for f, t, p in flights:
            ad_dict[f].append((t, p))
            ends.add(t)

        print(ad_dict)
        print(ends)
        if dst not in ends:
            return -1
        heap = [(0, src, 0)]
        while len(heap):
            print(heap)
            cost, position, stops = heappop(heap)
            print(position, position == dst, stops)
            if position == dst:
                return cost
            if stops > k:
                continue
            for t, p in ad_dict[position]:
                heappush(heap, (cost+p, t, stops+1))

        return -1


in_n = 13
# in_flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,
# 88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,
# 11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,
# 7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,
# 88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
in_flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
in_src = 10
in_dst = 1
in_k = 10
a = Solution()
print(a.findCheapestPrice(in_n, in_flights, in_src, in_dst, in_k))


"""

Make an adjacency list marking all the nodes the person can go to at how much distance
Use heap to get the the next stop according to the cheapest route that can be taken and add the next nodes the flight 
can take us using the adjacency list till the destination is reached

"""
