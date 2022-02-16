"""

---> First Unique Character in a String
---> Easy

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = {}
        dup = ""
        for i in range(len(s)):
            if s[i] in ans:
                ans.pop(s[i])
                dup += s[i]
            elif s[i] not in dup:
                ans[s[i]] = i
        print(dup)
        return min(ans.values()) if len(ans) != 0 else -1


in_s = "aadadaad"
a = Solution()
print(a.firstUniqChar(in_s))


"""
Keep track of the unique words and and duplicate words

Complexities:
Time -> O(N)
Space -> O(N)

"""
