"""

---> Single Number III
---> Medium

"""


class Solution:
    def singleNumber(self, nums):
        result, ele1, ele2 = 0, 0, 0

        for i in nums:
            result = result ^ i

        bitmask = result & -result  # Will give the rightmost bit which is different in the 2 numbers which don't
        # have a duplicate which can be used to distinguish between the numbers as one will & to 0 and other to bitmask
        for i in nums:
            if bitmask & i == 0:
                ele1 ^= i
                # print("if", i, ele1)
            else:
                ele2 ^= i
                # print("else", i, ele2)

        return [ele1, ele2]


in_nums = [1, 2, 1, 2, 992, 673]
a = Solution()
print(a.singleNumber(in_nums))

"""

Find the rightmost bit which distinguishes both the numbers i.e. one will & up to 0 and other to bitmask
Can be found as xor of all numbers & -(xor of all numbers) as xor of all numbers will give 1 to that place and 
compliment of that would give 1 to that place and 0 to others

"""
