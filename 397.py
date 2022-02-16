"""

---> Integer Replacement
---> Medium

"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        # Memorization
        ans = {1: 0}

        def helper(rem_n):
            if rem_n not in ans:
                if rem_n % 2:
                    ans[rem_n] = min(helper(rem_n - 1), helper(rem_n + 1)) + 1
                else:
                    ans[rem_n] = helper(rem_n/2) + 1
            return ans[rem_n]

        return helper(n)

    def integerReplacement_sol2(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return ans


in_n = 7
a = Solution()
print(a.integerReplacement(in_n))
# print(a.integerReplacement_sol2(in_n))


"""

Simple DP array with 3 conditions
Complexities:
Time -> O()
Space -> O(N)

Sol2 Reference - https://leetcode.com/problems/integer-replacement/discuss/87948/Python-O(log-n)-time-O(1)-space-with-explanation-and-proof

Complexities:
Time -> O(logN)
Space -> O(1)

"""
