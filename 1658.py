"""

---> Minimum Operations to Reduce X to Zero
---> Medium

"""
import math
from collections import defaultdict


class Solution:
    def minOperations(self, nums, x: int) -> int:
        sub_arr_sum, n, curr_sum = sum(nums) - x, len(nums), 0
        sum_dict = defaultdict()
        num_count = -1 * math.inf
        if sub_arr_sum == 0:
            return n
        for index, num in enumerate(nums):
            curr_sum += num
            if curr_sum == sub_arr_sum:
                num_count = max(num_count, index + 1)
                print("1-> ", num_count)
            if curr_sum - sub_arr_sum in sum_dict:
                num_count = max(num_count, index - sum_dict[curr_sum - sub_arr_sum])
                print("2-> ", num_count)
            if curr_sum not in sum_dict:
                sum_dict[curr_sum] = index
        return n - num_count if num_count != -1 * math.inf else -1


in_nums = [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
# in_nums = [3, 2, 20, 1, 1, 3]
in_x = 134365
a = Solution()
print(a.minOperations(in_nums, in_x))


"""

Removing leftmost and rightmost elements to get a sum of x is equal to finding a continuous sub-array with 
total sum of the array - x

"""
