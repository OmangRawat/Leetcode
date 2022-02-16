"""

---> Minimum Swaps to Make Strings Equal
---> Medium

"""


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        def is_xy(char1, char2):
            return char1 == 'x' and char2 == 'y'

        def is_yx(char1, char2):
            return char1 == 'y' and char2 == 'x'

        xy = sum(map(is_xy, s1, s2))
        yx = sum(map(is_yx, s1, s2))

        if xy % 2 != yx % 2:
            return -1

        return xy // 2 + yx // 2 + xy % 2 + yx % 2


in_s1 = "xy"
in_s2 = "yx"
a = Solution()
print(a.minimumSwap(in_s1, in_s2))


"""

Check respective indexes and if their is a pair of xy and yx then it will take 2 changes else if it is xx or yy then it 
will take 1 change

"""
