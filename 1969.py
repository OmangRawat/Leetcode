"""

---> Minimum Non-Zero Product of the Array Elements
---> Medium

"""


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        no_of_numbers = 2**p - 2

        return ((pow(no_of_numbers, no_of_numbers//2, mod)) * (no_of_numbers + 1)) % mod


in_p = 3
a = Solution()
print(a.minNonZeroProduct(in_p))


"""

No. of numbers is 2^p-1 and remove the last element then their make pairs and each would give product 2^p-2 then total 
pairs are (2^p-2)/2 and product with last number
Reference - https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/discuss/1404240/Well-Explained-oror-Clean-and-Concise-oror-98-faster

"""
