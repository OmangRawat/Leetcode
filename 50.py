"""

---> Pow(x, n)
---> Medium

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            ans = 1
            while n:
                if n % 2:
                    ans *= x
                x *= x
                n //= 2
            return ans
        else:
            return self.myPow(1 / x, -1 * n)


in_x = 2
in_n = 10
a = Solution()
print(a.myPow(in_x, in_n))
