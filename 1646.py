"""

---> Get Maximum in Generated Array
---> Easy

"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 2)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + nums[(i // 2) + 1] * (i % 2)
        return max(nums[:n + 1])


in_n = 7
a = Solution()
print(a.getMaximumGenerated(in_n))


"""

nums array as given in ques the pattern is nums[i] = nums[i//2] for even i or nums[i] = nums[i//2] + nums[i//2 + 1]
so just use i%2
Reference - https://leetcode.com/problems/get-maximum-in-generated-array/discuss/1017760/Python-Simulate-process-explained

Complexities:
Time -> O(N)
Space -> O(N)

"""
