"""

---> Longest Repeating Character Replacement
---> Medium

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, ans = 0, 0
        freq = {}
        for end in range(len(s)):
            if s[end] not in freq:
                freq[s[end]] = 0

            freq[s[end]] += 1
            curr_len = end - start + 1

            if curr_len - max(freq.values()) <= k:
                ans = max(ans, curr_len)
            else:
                freq[s[start]] -= 1
                if not freq[s[start]]:
                    freq.pop(s[start])
                start += 1
            # print(start, end, curr_len, freq)
        return ans


in_s = "AACBABBA"
in_k = 1
a = Solution()
print(a.characterReplacement(in_s, in_k))


"""

Keep track of the start of needed substring and the current char being checked.
Keep track of frequencies of the chars in the substring.
Move the start point ahead as the changes that can be made get finished.

"""
