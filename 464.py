"""

---> Can I Win
---> Medium

"""
from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def check(bitmask, curr_total):
            if curr_total >= desiredTotal and bitmask != 0:     # Game ended and there was at least one chance played
                return False
            for i in range(1, maxChoosableInteger + 1):
                if (bitmask >> (i - 1)) & 1 == 0:   # If that particular integer has not been used before
                    if not check(bitmask | (1 << (i - 1)), curr_total + i):     # Use that integer set the bitmask
                        return True                                             # and check the condition if the
            return False                                                        # game is still going on

        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False

        return check(0, 0)


in_int = 10
in_total = 11
a = Solution()
print(a.canIWin(in_int, in_total))


"""

Check for each integer such that it gives best possible result
Use bitmask by setting the bits of the places the integer is used and keep track of the current sum till it is greater 
than the desired total

"""
