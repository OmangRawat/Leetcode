"""

---> Construct K Palindrome Strings
---> Medium

"""
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        freq = Counter(s)
        odd_ele = 0

        for i in freq:
            if freq[i] % 2 != 0:
                odd_ele += 1

        if k < odd_ele:
            return False

        return True


in_s = "annabelle"
in_k = 2
a = Solution()
print(a.canConstruct(in_s, in_k))


"""
Check for the chars which have odd frequency because they will take one word so if the odd freq is greater than k then 
the number of divisions will be greater too
"""
