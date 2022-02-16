"""

---> Find K Pairs with Smallest Sums
---> Medium

"""
from heapq import *


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        heap = []
        heapify(heap)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            ele1, ele2 = nums1[i], nums2[j]
            if len(heap) == k:
                if ele1 + ele2 > -heap[0][0]:
                    i += 1
                    j = 0
                    continue
                else:
                    heappop(heap)
                    heappush(heap, (-(ele1 + ele2), ele1, ele2))
            else:
                heappush(heap, (-(ele1 + ele2), ele1, ele2))
            j += 1
            if j >= len(nums2):
                j = 0
                i += 1

        ans = []
        while heap:
            _, ele1, ele2 = heappop(heap)
            ans.append([ele1, ele2])
        return ans

    def kSmallestPairs_sol2(self, nums1, nums2, k: int):
        ans = []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0)}
        # k = min(k, len(nums1) * len(nums2))
        while k > 0:
            k -= 1
            _, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


in_nums1 = [1, 2]
in_nums2 = [3]
in_k = 3
a = Solution()
print(a.kSmallestPairs(in_nums1, in_nums2, in_k))
print(a.kSmallestPairs_sol2(in_nums1, in_nums2, in_k))


"""

Approach 1:
Take a heap which wll store the sum of the elements in negative and the elements, Insert directly when the length of 
heap is smaller than k, else check the top element and replace it if it has smaller sum than the max sum in heap
Iterate through the arrays once through one array for every element in the other

Approach 2:
Take a heap with sum of the array and the elements needed. Pop the smallest sum in the heap and add in the visited and 
ans array
Iterate through the first array for every element n the second array

Reference - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/1642090/Python-Priority-Queue-heapq-Accepted
"""
