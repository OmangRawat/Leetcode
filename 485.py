"""

---> Max Consecutive Ones
---> Easy

"""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        ans = 0
        counter = 0

        for i in nums:
            if i == 0:
                ans = max(ans, counter)
                counter = 0
            else:
                counter += 1
        ans = max(ans, counter)
        
        return ans


in_nums = [1, 1, 0, 1, 1, 1]
a = Solution()
print(a.findMaxConsecutiveOnes(in_nums))
