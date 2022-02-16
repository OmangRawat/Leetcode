"""

---> Minimum Operations to Make the Array Increasing
---> Easy

"""


class Solution:
    def minOperations(self, nums) -> int:
        ans, level = 0, 0
        for num in nums:
            if num <= level:
                level += 1
                ans += level - num
            else:
                level = num
        return ans


in_nums = [1, 5, 2, 4, 1]
a = Solution()
print(a.minOperations(in_nums))


"""

Set level to last number then check for how many 1s need to be added to next number i.e. (level + 1 - num)

"""
