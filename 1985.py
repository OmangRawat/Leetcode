"""

---> Find the Kth Largest Integer in the Array
---> Medium

"""
from heapq import *


class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        num_arr = [int(i) for i in nums]
        ans = sorted(num_arr)[-k]
        return str(ans)

    def kthLargestNumber_sol2(self, nums, k: int) -> str:
        nums = [-int(i) for i in nums]
        heapify(nums)
        for i in range(k - 1):
            heappop(nums)

        return f'{-nums[0]}'


in_nums = ["2", "21", "12", "1"]
in_k = 3
a = Solution()
print(a.kthLargestNumber(in_nums, in_k))
print(a.kthLargestNumber_sol2(in_nums, in_k))


"""
Approach 1:
Sort an array in ascending order and get the kth element from last

Approach 2:
Put all the negative of elements in a min heap then pop k - 1 ele the next element is the answer

Reference - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/discuss/1616089/%3A)-Python-Solution-(-heap-DS-)-%2B-Suitable-Comments-!
"""
