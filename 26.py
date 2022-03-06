"""

---> Remove Duplicates from Sorted Array
---> Easy

"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                k += 1
                nums[k] = nums[i]
        return k + 1


in_nums = [1, 2, 2, 3]
a = Solution()
print(a.removeDuplicates(in_nums))
