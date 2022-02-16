"""

---> Longest Arithmetic Subsequence of Given Difference
---> Medium

"""


class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        ans = {}
        for i in arr:
            ans[i] = ans.get(i - difference, 0) + 1
            print(i, ans)
        return max(ans.values())


in_arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
in_difference = -2
a = Solution()
print(a.longestSubsequence(in_arr, in_difference))


"""

ans stores all the values that have come before and max array that can be made till there
runs a for loop checking if the number needed has come before
Reference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/discuss/398216/Python-4-lines

Complexities:
Time -> O(N)
Space -> O(N)

"""
