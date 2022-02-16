"""

---> Find All Duplicates in an Array
---> Medium

"""


class Solution:
    def findDuplicates(self, nums):
        for i in nums:
            i = abs(i)
            if nums[i - 1] < 0:
                yield i
                continue
            nums[i - 1] *= -1


in_nums = [4, 3, 2, 7, 8, 2, 3, 1, 2]
a = Solution()
ans = [i for i in a.findDuplicates(in_nums)]
print(ans)
