"""

---> Minimum Insertions to Balance a Parentheses String
---> Medium

"""


class Solution:
    def minInsertions(self, s: str) -> int:
        open_brackets = 0
        insertions_needed = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_brackets += 1
            else:
                if i == len(s) - 1:
                    insertions_needed += 1
                elif s[i + 1] != ')':
                    insertions_needed += 1
                else:
                    i += 1

                if open_brackets:
                    open_brackets -= 1
                else:
                    insertions_needed += 1
            i += 1

        insertions_needed += 2 * open_brackets

        return insertions_needed


in_s = "))())("
a = Solution()
print(a.minInsertions(in_s))


"""
Keep track of number of (, if you get a ) then check if their are more elements after it, if not then ans + 1 else check 
if the next bracket is ) then decrease a ( else ans + 1
At last add 2 * remaining open brackets to ans
"""
