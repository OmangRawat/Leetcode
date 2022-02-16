"""

---> Find the Longest Substring Containing Vowels in Even Counts
---> Medium

"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        ind_dict = {0: -1}
        state, ans = 0, 0
        for i, char in enumerate(s):
            if char in vowels:
                state ^= vowels[char]
            if not (state in ind_dict):
                ind_dict[state] = i

            ans = max(ans, i - ind_dict[state])

        return ans


in_s = "leetcodeisgreat"
a = Solution()
print(a.findTheLongestSubstring(in_s))


"""
Reference: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/1500440/Python3-O(n)-Solution-with-Explanations
"""
