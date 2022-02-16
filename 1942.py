"""

---> The Number of the Smallest Unoccupied Chair
---> Medium

"""
from heapq import *


class Solution:
    def smallestChair(self, times, targetFriend: int) -> int:
        chair_occupied = [-1] * len(times)
        heap = []
        max_chair_needed = 0
        time_record = []

        for i, time in enumerate(times):
            time_record.extend([(time[0], True, i), (time[1], False, i)])

        time_record.sort()

        for time, is_arrival, person in time_record:
            if person == targetFriend:
                return heap[0] if heap else max_chair_needed
            elif is_arrival:
                if heap:
                    chair_occupied[person] = heap[0]
                    heappop(heap)
                else:
                    chair_occupied[person] = max_chair_needed
                    max_chair_needed += 1
            else:
                heappush(heap, chair_occupied[person])
        return max_chair_needed


in_times = [[3, 10], [1, 5], [2, 6]]
in_targetFriend = 0
a = Solution()
print(a.smallestChair(in_times, in_targetFriend))


"""

Approach 1:
Keep track of the person occupying which chair, Divide the times into arrival and leaving of each person. Check if a 
chair is empty then assign the chair to that person else provide them with a new chair and if it is a person leaving 
then put the chair in heap which will sort it and ready to assign to next person
Reference - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/discuss/1643525/Simple-Python-solution-with-explanation

"""
