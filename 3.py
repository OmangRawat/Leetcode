"""

---> Longest Substring Without Repeating Characters
---> Medium

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_positions = {}
        start = curr_position = max_len = curr_len = 0
        if len(s) == 1:
            return 1
        for i in s:
            if i in char_positions:
                if char_positions[i] > start:
                    start = char_positions[i]
                curr_len = curr_position - start
            curr_len += 1
            curr_position += 1
            char_positions[i] = curr_position
            if curr_len > max_len:
                max_len = curr_len
        return max_len


in_s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(in_s))
