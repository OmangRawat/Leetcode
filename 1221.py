"""

---> Split a String in Balanced Strings
---> Easy

"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        difference = 0
        ans = 0
        for i in s:
            if i == "L":
                difference += 1
            else:
                difference -= 1
            if difference == 0:
                ans += 1
        return ans


in_s = "RLLLLRRRLR"
a = Solution()
print(a.balancedStringSplit(in_s))


"""
To divide the string into balanced string increase difference by 1 for L and decrease by 1 for R, Increase ans whenever 
diff = 0
"""
