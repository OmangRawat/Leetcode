"""

---> Last Stone Weight
---> Easy

"""
import bisect
import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1 and heap[0] != 0:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
            print(heap)
        return -heap[0]

    def lastStoneWeight_sol2(self, stones) -> int:
        stones.sort()
        while len(stones) > 1:
            bisect.insort(stones, stones.pop() - stones.pop())
            print(stones)
        return stones[0]


in_stones = [2, 7, 4, 1, 8, 1]
a = Solution()
print(a.lastStoneWeight(in_stones))
print(a.lastStoneWeight_sol2(in_stones))


"""

Approach 1:
Make a min heap of negative o weights i.e. somehow same max heap, get the 2 top elements check for diff and append it 
back if their is something remaining till len smaller than 1 and heap[0] != 0

Approach 2:
Use bisect.insort after sorting the array, take top 2 elements subtract and add it back, it will add the new element 
properly so that the resultant array still remains sorted

Reference - https://leetcode.com/problems/last-stone-weight/discuss/294956/JavaC%2B%2BPython-Priority-Queue

"""
