"""

---> Count Array Pairs Divisible by K
---> Hard

"""
from collections import Counter
from math import gcd


class Solution:
    def countPairs(self, nums, k):
        counter = Counter(gcd(x, k) for x in nums)
        ans = 0
        for i in counter:
            for j in counter:
                if i <= j and not i * j % k:
                    ans += counter[i] * counter[j] if i < j else counter[i] * (counter[i] - 1) // 2
        return ans


in_nums = [1, 2, 3, 4, 5]
in_k = 2
a = Solution()
print(a.countPairs(in_nums, in_k))
