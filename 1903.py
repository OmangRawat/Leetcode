"""

---> Largest Odd Number in String
---> Easy

"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd_digit = len(num) - 1
        while last_odd_digit > -1 and int(num[last_odd_digit]) % 2 == 0:
            last_odd_digit -= 1

        return num[:last_odd_digit + 1]


in_num = "35427"
a = Solution()
print(a.largestOddNumber(in_num))


"""
Check for the last odd digit in the string
"""
