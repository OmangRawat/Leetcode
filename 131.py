"""

---> Palindrome Partitioning
---> Medium

"""
from functools import lru_cache


class Solution:
    @lru_cache()
    def partition(self, string: str):
        if not string:
            return [[]]
        ans = []
        for i in range(1, len(string) + 1):
            if string[:i] == string[:i][::-1]:
                for suffix in self.partition(string[i:]):
                    ans.append([string[:i]] + suffix)
        return ans


in_s = "aab"
a = Solution()
print(a.partition(in_s))
