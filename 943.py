"""

---> Find the Shortest Superstring
---> Hard

"""
from functools import lru_cache


class Solution:
    def shortestSuperstring(self, words):
        @lru_cache()
        def not_common_suffix(s1, s2):
            for idx in range(min(len(s1), len(s2)), 0, -1):
                if s2.startswith(s1[-idx:]):
                    return s2[idx:]
            return s2

        @lru_cache()
        def dfs(bitmask, i):
            if bitmask + 1 == 1 << n:
                return ""
            return min([not_common_suffix(words[i], words[j]) + dfs(bitmask | 1 << j, j) for j in range(n) if not (bitmask & 1 << j)], key=len)

        n = len(words)
        return min([words[i] + dfs(1 << i, i) for i in range(n)], key=len)


in_words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
a = Solution()
print(a.shortestSuperstring(in_words))
