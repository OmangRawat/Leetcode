""""

---> Maximum Nesting Depth of the Parentheses
---> Easy

"""


class Solution:
    def maxDepth(self, s: str) -> int:
        stack, ans = [], 0
        for i in s:
            if i == "(":
                stack.append(i)
                ans = max(ans, len(stack))
            elif i == ")":
                stack.pop()
        return ans

    def maxDepth_sol2(self, s: str) -> int:
        ans, cur = 0, 0
        for i in s:
            if i == '(':
                cur += 1
                ans = max(ans, cur)
            if i == ')':
                cur -= 1
        return ans


in_s = "(1)+((2))+(((3)))"
a = Solution()
print(a.maxDepth(in_s))
print(a.maxDepth_sol2(in_s))


"""
Approach 1:
Use a simple stack push for (, pop for )

Complexities:
Time -> O(N)
Space -> O(N)


Approach 2:

Complexities:
Time -> O(N)
Space -> O(1)

"""
