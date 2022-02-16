"""

---> N-th Tribonacci Number
---> Easy

"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        t0 = 0
        t1 = 1
        t2 = 1
        for i in range(n - 2):
            tn = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = tn
        return tn


in_n = 25
a = Solution()
print(a.tribonacci(in_n))

"""

Reference - https://leetcode.com/problems/n-th-tribonacci-number/discuss/1482728/C%2B%2BPython-2-solutions%3A-DP-Matrix-exponential-Picture-explained-Clean-and-Concise

Complexities:
Time -> O(N)
Space -> O(1)
For big values of N could be prob there is a sol in the referenced link

"""
