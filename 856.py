"""

---> Score of Parentheses
---> Medium

"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, cur = [], 0
        for i in s:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
            print(stack, cur)
        return cur

    def scoreOfParentheses_sol2(self, s: str) -> int:
        ans, level = 0, 0
        for i, j in zip(s, s[1:]):
            print(i, j)
            if i + j == '()':
                ans += 2 ** level
            level += 1 if i == '(' else -1
        return ans


in_s = '(((()())))'
a = Solution()
# print(a.scoreOfParentheses(in_s))
print(a.scoreOfParentheses_sol2(in_s))


"""
Reference - https://leetcode.com/problems/score-of-parentheses/discuss/141777/C%2B%2BJavaPython-O(1)-Space

Approach 1:
Input 0 for every open bracket thus 0 will show the level and append the last current for every A + B

Complexities:
Time -> O(N)
Space -> O(N)


Approach 2:
For every time () comes double it bcz it would be the innermost one if it has some outside else +1 and -1 if closed

Complexities:
Time -> O(N)
Space -> O(1)

"""
