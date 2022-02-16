"""

---> Sell Diminishing-Valued Colored Balls
---> Medium

"""
from heapq import *


class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        heap = [-i for i in inventory]
        heapify(heap)
        ans = 0
        while orders > 0:
            curr_order = heappop(heap)
            if len(heap) == 0:
                heappush(heap, -1)
            while orders > 0 and -curr_order >= -heap[0] - 1:
                ans -= curr_order
                curr_order += 1
                orders -= 1
                ans % (10**9 + 7)
            heappush(heap, curr_order)
        return ans


in_inventory = [1000000000]
in_orders = 1000000000
a = Solution()
print(a.maxProfit(in_inventory, in_orders))
