"""

--- > Minimum Replacements to Sort the Array
--- > Hard

"""
from math import ceil


class Solution:
    def minimumReplacement(self, nums):
        # Faster than recursion
        n = len(nums)
        ops = 0
        max_limit = nums[n - 1]
        for ind in range(n - 2, -1, -1):
            curr_num = nums[ind]
            min_divs = ceil(curr_num / max_limit)
            ops += min_divs - 1
            max_limit = curr_num // min_divs

        return ops

    def minimumReplacement_2(self, nums):
        # Slower (no need of forming extra vars and space)
        def get_operations(index, last):
            nonlocal ops, max_limit
            if index == -1:
                return
            else:
                curr_num = nums[index]
                min_divs = ceil(curr_num / last)
                ops += (min_divs - 1)
                max_limit = curr_num // min_divs
                get_operations(index - 1, max_limit)

        n = len(nums)
        ops = 0
        max_limit = nums[n - 1]
        get_operations(n - 1, max_limit)
        return ops


in_nums = [1, 2, 3, 4, 5]
a = Solution()
print(a.minimumReplacement(in_nums))
