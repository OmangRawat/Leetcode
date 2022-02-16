"""

---> Evaluate Reverse Polish Notation
---> Medium

"""


class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for char in tokens:
            if char in "+-*/":
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(eval(b + char + a))))
            else:
                stack.append(char)
        return int(stack.pop())


in_tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
a = Solution()
print(a.evalRPN(in_tokens))


"""

Stack stores all str of ints and whenever an operation comes pops last 2 and returns evaluated ans

Complexities:
Time -> O(N)
Space -> O(N)

"""


