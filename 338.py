"""

---> Counting Bits
---> Easy

"""


class Solution:
    def count_bits(self, n: int):
        ans = [0]
        while len(ans) <= n:
            ans += [i + 1 for i in ans]
        return ans[:n + 1]


in_n = 5
a = Solution()
print(a.count_bits(in_n))


"""
For every next shift of one to right the result would be +1 of the already existing array because between 2^n to 2^(n+1)
there are 2^n numbers
Reference - https://leetcode.com/problems/counting-bits/discuss/79538/Simple-Python-Solution

Complexities:
Time -> O(n)
Space -> O(n)

"""
