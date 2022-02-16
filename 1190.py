"""

---> Reverse Substrings Between Each Pair of Parentheses
---> Medium

"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                add = stack.pop()[::-1]
                print(add)
                stack[-1] += add
            else:
                stack[-1] += char
            # print(stack)
        return stack.pop()


in_s = "(ed(et(oc))el)"
a = Solution()
print(a.reverseParentheses(in_s))


"""

Push into stack and pop all as a ) comes 
Reference - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/383670/JavaC%2B%2BPython-Tenet-O(N)-Solution

Complexities:
Time -> O(N^2)
Space -> O(N)

"""
