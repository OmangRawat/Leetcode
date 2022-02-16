"""

---> Number of Sets of K Non-Overlapping Line Segments
---> Medium

"""
from functools import lru_cache


class Solution:
    def numberOfSets(self, n, k) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def helper(start, rem_k, div_ongoing):
            if start == n - 1:
                if rem_k:
                    return 0
                else:
                    return 1
            ans = 0
            if div_ongoing:
                ans += helper(start + 1, rem_k, div_ongoing)
                ans += helper(start + 1, rem_k, not div_ongoing)
                if rem_k > 0:
                    ans += helper(start + 1, rem_k - 1, div_ongoing)
                ans %= mod
            else:
                ans += helper(start + 1, rem_k, div_ongoing)
                if rem_k > 0:
                    ans += helper(start + 1, rem_k - 1, not div_ongoing)
                ans %= mod
            print(start, rem_k, div_ongoing, ans)
            return ans

        return helper(0, k, False)


in_n = 4
in_k = 2
a = Solution()
print(a.numberOfSets(in_n, in_k))


"""

Divide every division into rem_k parts if possible or rem_k - 1 parts
Time can be optimized by keeping a dictionary
Reference - https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/discuss/898844/Top-Down-DP-or-O(n*k)

Complexities:
Time -> O(N*K)
Space -> O(1)


Reference - https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/discuss/898830/Python-O(N)-Solution-with-Prove

Complexities:
Time -> O(N)
Space -> O(1)

"""
