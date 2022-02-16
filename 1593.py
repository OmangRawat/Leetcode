"""

---> Split a String Into the Max Number of Unique Substrings
---> Medium

"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, path):
            nonlocal ans
            if n - start + len(path) <= ans:
                return
            if start == n:
                ans = max(ans, len(path))
                return
            for i in range(start + 1, n + 1):
                if s[start:i] not in path:
                    backtrack(i, path | {s[start:i]})

        n, ans = len(s), 0
        backtrack(0, set())

        return ans


in_s = "ababccc"
a = Solution()
print(a.maxUniqueSplit(in_s))
