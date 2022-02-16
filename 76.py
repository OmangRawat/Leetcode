"""

---> Minimum Window Substring
---> Hard

"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        required_ele = len(counter)
        ele_in_substring = 0
        substring_start = 0
        min_window_length = float("inf")
        min_substring = ""

        for substring_end in range(len(s)):
            if s[substring_end] in counter:
                counter[s[substring_end]] -= 1
                if counter[s[substring_end]] == 0:
                    ele_in_substring += 1

            while ele_in_substring == required_ele and (s[substring_start] not in counter or counter[s[substring_start]] < 0):
                if s[substring_start] in counter:
                    counter[s[substring_start]] += 1
                substring_start += 1

            if ele_in_substring == required_ele and (substring_end - substring_start + 1) < min_window_length:
                min_window_length = substring_end - substring_start + 1
                min_substring = s[substring_start:substring_end + 1]

        return min_substring


in_s = "ADOBECODEBANC"
in_t = "ABC"
a = Solution()
print(a.minWindow(in_s, in_t))


"""
Reference - https://leetcode.com/problems/minimum-window-substring/discuss/1713067/Python%3A-O(T)-Space-and-O(N)-Time
"""
