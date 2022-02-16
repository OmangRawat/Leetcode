"""

---> Check if a Parentheses String Can Be Valid
---> Medium

"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        changeable_brackets = open_brackets = close_brackets = 0

        for i in range(len(s)):
            if locked[i] == '0':
                changeable_brackets += 1
            elif s[i] == '(':
                open_brackets += 1
            elif s[i] == ')':
                close_brackets += 1

            if changeable_brackets + open_brackets - close_brackets < 0:
                return False

        changeable_brackets = open_brackets = close_brackets = 0

        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                changeable_brackets += 1
            elif s[i] == '(':
                open_brackets += 1
            elif s[i] == ')':
                close_brackets += 1

            if changeable_brackets - open_brackets + close_brackets < 0:
                return False

        return True


in_s = "))()))"
in_locked = "010100"
a = Solution()
print(a.canBeValid(in_s, in_locked))


"""
We should have equal no. of open and closed thus multiple of 2
Keep track of changeable open and closed brackets
In forward iteration, we check if we have too many closed brackets that we can't take care off then return False
In backward iteration, we check if we have too many open brackets that we can't take care off then return False

Reference - https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646582/Python3-Java-C%2B%2B-Counting-Brackets-O(n)
"""
