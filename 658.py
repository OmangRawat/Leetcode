"""

---> Find K Closest Elements
---> Medium

"""
import bisect
import math
from heapq import *


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        heap = []

        for ele in arr:
            dist = abs(ele - x)

            if len(heap) < k:
                heappush(heap, (-1 * dist, ele))
            else:
                if -1 * heap[0][0] > dist:
                    heappop(heap)
                    heappush(heap, (-1 * dist, ele))

        return sorted([ele for _, ele in heap])

    def findClosestElements_sol2(self, arr, k: int, x: int):
        index = bisect.bisect_left(arr, x)
        left, right, count, left_val, right_val = index - 1, index, 0, math.inf, math.inf
        result = []
        while count < k:
            left_val = abs(arr[left] - x) if left >= 0 else math.inf
            right_val = abs(arr[right] - x) if right <= len(arr) - 1 else math.inf
            print('left: {}, right: {}, leftVal: {}, rightVal:{} x: {}'.format(left, right, left_val, right_val, x))
            if left_val <= right_val:
                result.insert(0, arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            count += 1
        return result


in_arr = [1, 2, 3, 4, 5]
in_k = 4
in_x = -1
a = Solution()
# print(a.findClosestElements(in_arr, in_k, in_x))
print(a.findClosestElements_sol2(in_arr, in_k, in_x))


"""
Approach 1:
Traverse the array and keep track of k closest elements till there using the abs distance from the element x in a min 
heap, pop out the top one to replace if you find a closer element
Reference - https://leetcode.com/problems/find-k-closest-elements/discuss/1145950/Python-Heap

Complexities:
Time -> O(NlogK)
Space -> O(K)

Approach 2:
In the sorted array find the place of the element x the closest element to it will be either on its left or right, check 
whichever is closer and add to the array till the length of the array becomes k
Reference - https://leetcode.com/problems/find-k-closest-elements/discuss/1446787/python-soluton-using-python-bisect-time-O(logN)-%2BO(K)-space-O(1)

Complexities:
Time -> O(logN) +O(K)
Space -> O(1)

"""
