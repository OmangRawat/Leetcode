"""

---> Different Ways to Add Parentheses
---> Medium

"""
# import bigO


class Solution:
    def diff_ways_to_compute(self, expression: str):
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i in range(len(expression)):
            if expression[i] in "-+*":
                left = self.diff_ways_to_compute(expression[:i])
                right = self.diff_ways_to_compute(expression[i + 1:])
                # print(expression[i], i, left, right)
                for j in left:
                    for k in right:
                        if expression[i] == '+':
                            ans.append(j + k)
                        elif expression[i] == '-':
                            ans.append(j - k)
                        elif expression[i] == '*':
                            ans.append(j * k)
                # print(ans)
                # if expression[i] == '+':
                #     ans.append(left[0] + right[0])
                # elif expression[i] == '-':
                #     ans.append(left[0] - right[0])
                # elif expression[i] == '*':
                #     ans.append(left[0] * right[0])
        return ans


in_expression = "2*3-4*5"
a = Solution()
print(a.diff_ways_to_compute(in_expression))
# lib = bigO.BigO()
# complexity = lib.test_all(a.diff_ways_to_compute(in_expression))
# print(complexity)

"""

Divide expression into left, right and operation for every operation
Use divide and conquer and compute left and write by recursive calling
Time can be reduced by using dictionary to keep track
Reference - https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/520018/Easy-understand-DandC-solution-no-helper-function-needed-Pattern-example

Complexities:
Time -> 
Space -> 

"""
