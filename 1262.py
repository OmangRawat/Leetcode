"""

---> Greatest Sum Divisible by Three
--> Medium

"""
import math


class Solution:
    def maxSumDivThree(self, nums) -> int:
        total = 0
        rem1 = [math.inf, math.inf]
        rem2 = [math.inf, math.inf]

        for num in nums:
            if num % 3 == 1:
                if num < rem1[0]:
                    rem1[0], rem1[1] = num, rem1[0]
                elif num < rem1[1]:
                    rem1[1] = num
            elif num % 3 == 2:
                if num < rem2[0]:
                    rem2[0], rem2[1] = num, rem2[0]
                elif num < rem2[1]:
                    rem2[1] = num
            total += num

        if total % 3 == 1:
            if math.inf in rem2:
                return total - rem1[0]
            total -= min(sum(rem2), rem1[0])
        elif total % 3 == 2:
            if math.inf in rem1:
                return total - rem2[0]
            total -= min(sum(rem1), rem2[0])

        return total


in_nums = [3, 6, 5, 1,  8]
a = Solution()
print(a.maxSumDivThree(in_nums))


"""

We only need to keep track of 2 minimum numbers with remainder 1 and 2 then check if the total sum has a remainder 1 
then take minimum of the smallest number with remainder 1 or sum of smallest 2 with remainder 2 else if total has 
remainder 2 then take minimum of sum of 2 smallest with remainder 1 or smallest with remainder 2

Reference - https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/1646188/Python-O(N)-without-DP-O(1)-space

Complexities:
Time -> O(N)
Space -> O(1)

"""
