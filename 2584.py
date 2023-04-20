"""

---> Split the Array to Make Coprime Products
---> Hard

"""

from math import prod, gcd


class Solution:
    def findValidSplit(self, nums):
        n = len(nums)
        left_prod = 1
        index = 0

        while index < n - 1:
            left_prod *= nums[index]
            j = index + 1

            # if after index there is no number having a co-divisor then it is the ans
            while j < n and gcd(left_prod, nums[j]) == 1:
                j += 1
            if j == n:
                return index

            # if there is a number having co-divisor it should also be on let for a coprime division
            left_prod *= prod(nums[index + 1:j])
            index = j

        return -1


in_nums = [4, 7, 8, 15, 3, 5]
a = Solution()
print(a.findValidSplit(in_nums))
