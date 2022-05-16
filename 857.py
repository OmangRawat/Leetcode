"""

---> Minimum Cost to Hire K Workers
---> Hard

"""
from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(self, quality, wage, k: int) -> float:
        workers = []
        ans = float('inf')
        ratio_sum = 0
        heap = []

        for w, q in zip(wage, quality):
            workers.append([float(w) / q, q])
        workers.sort()

        for r, q in workers:
            heappush(heap, -q)
            ratio_sum += q

            if len(heap) > k:
                ratio_sum += heappop(heap)

            if len(heap) == k:
                ans = min(ans, ratio_sum * r)

        return ans


in_quality = [3, 1, 10, 10, 1]
in_wage = [4, 8, 2, 2, 7]
in_k = 3
a = Solution()
print(a.mincostToHireWorkers(in_quality, in_wage, in_k))


"""

Use fractional rates to sort as the rates that come after a particular weight would have rate greater than previous ones
Then use heap to get best quality

"""
