"""

---> Reduce Array Size to The Half
---> Medium

"""
from collections import Counter
from heapq import *


class Solution:
    def minSetSize(self, arr) -> int:
        freq = Counter(arr)
        freq_arr = sorted(freq.values(), reverse=True)
        length = len(arr)
        new_length = length
        needed_length = length // 2
        count = 0
        i = 0
        while i < len(freq_arr):
            if new_length <= needed_length:
                return count
            else:
                new_length -= freq_arr[i]
                count += 1
            i += 1

    def minSetSize_sol2(self, arr) -> int:
        freq = Counter(arr)
        heap = [(-values, key) for key, values in freq.items()]

        heapify(heap)

        length = len(arr)
        new_length = length
        needed_length = length // 2

        for i in range(len(heap)):
            reduce = -1 * heappop(heap)[0]
            new_length = new_length - reduce
            if new_length <= needed_length:
                return i + 1


in_arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
a = Solution()
print(a.minSetSize(in_arr))
print(a.minSetSize_sol2(in_arr))


"""

Approach 1:
Count freq of all the elements then remove the elements by removing ones with higher freq first to get the array of 
length smaller than half
Reference - https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1598785/Python-O(nlogn)-time-and-O(n)-space-solution

Approach 2:
Count elements put in heap which will sort it according to freq then remove one by one
Reference - https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1451772/Python-heap-solution

"""
