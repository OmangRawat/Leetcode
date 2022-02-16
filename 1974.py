"""

---> Minimum Time to Type Word Using Special Typewriter
---> Easy

"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        prev = "a"
        for curr in word:
            diff = abs(ord(curr) - ord(prev))
            if diff > 13:
                diff = 26 - diff
            time += diff + 1
            prev = curr
        return time


in_word = "zjpc"
a = Solution()
print(a.minTimeToType(in_word))


"""
Check for whichever takes smaller time to reach next char clockwise or anti then add 1 for writing
"""
