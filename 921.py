"""

---> Minimum Add to Make Parentheses Valid
---> Medium

"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                count += 1
            # print(stack)
        return len(stack) + count

    def minAddToMakeValid_sol2(self, s: str) -> int:
        open, close = 0, 0
        for i in s:
            if close == 0 and i == ')':
                open += 1
            else:
                if i == '(':
                    close += 1
                else:
                    close -= 1
            # print(i, open, close)
        return open + close


in_s = "()))(("
a = Solution()
# print(a.minAddToMakeValid(in_s))
print(a.minAddToMakeValid_sol2(in_s))


"""
Approach 1:
Keep track of open brackets without a closing pair yet in stack and number of open bracket needed for every closed 
bracket without a pair in count variable
Reference - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/582230/Python-or-Beats-99-or-Very-easy-to-understand

Complexities:
Time -> O(N)
Space -> O(N)


Approach 2:
Open denotes number of open brackets needed and close the number of close bracket needed, when there is closed bracket
even though not needed increase number of open brackets needed and similar for closed
Reference - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/181132/C%2B%2BJavaPython-Straight-Forward-One-Pass


Complexities:
Time -> O(N)
Space -> O(1)

"""
