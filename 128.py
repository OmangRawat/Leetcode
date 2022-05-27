"""

---> Longest Consecutive Sequence
---> Medium

"""


class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums:
                curr = num
                while curr in nums:
                    ans = max(ans, curr - num + 1)
                    curr = curr + 1
        return ans


in_nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
a = Solution()
print(a.longestConsecutive(in_nums))


"""

For every number that doesn't have a number smaller than it find how many numbers are there in continuation with it

"""
