"""

---> Kth Smallest Element in a Sorted Matrix
---> Medium

"""
import bisect
from heapq import *


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        heap = []
        for row in matrix:
            for element in row:
                heappush(heap, element)
        k = k - 1
        while k:
            heappop(heap)
            k -= 1
        return heap[0]

    def kthSmallest_sol2(self, matrix, k: int) -> int:
        final_matrix = []
        for i in matrix:
            final_matrix += i
        return sorted(final_matrix)[k - 1]

    def kthSmallest_sol3(self, matrix, k: int) -> int:
        final_matrix = []
        for i in matrix:
            for j in i:
                bisect.insort(final_matrix, j)
        return final_matrix[k - 1]


in_matrix = [[1, 2], [1, 3]]
in_k = 2
a = Solution()
print(a.kthSmallest(in_matrix, in_k))
print(a.kthSmallest_sol2(in_matrix, in_k))
print(a.kthSmallest_sol3(in_matrix, in_k))


"""

Approach 1:
Put all the elements in a min heap and pop (k - 1) elements, next element will be the ans

Approach 2:
Make it a 2D array, Sort the array and return the (k - 1)th element 

Approach 3:
Use bisect and input all the elements in proper places to get the sorted array then take (k - 1)th element

"""
