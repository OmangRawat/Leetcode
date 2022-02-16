"""

---> Remove Duplicate Letters
---> Medium

"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        word_count = Counter(s)
        stack = []
        for i in s:
            if i not in set(stack):
                while stack and i < stack[-1] and word_count[stack[-1]] > 1:
                    char = stack.pop()
                    word_count[char] -= 1
                stack.append(i)
            else:
                word_count[i] -= 1
            # print(stack)

        return "".join(stack)


in_s = "dcbaccbc"
a = Solution()
print(a.removeDuplicateLetters(in_s))


"""
Input words in stack and if you get a letter with smaller value than the top most char in stack then pop the top element 
of stack if the letter would  still occur after the current letter i.e its count is still greater than 1
"""
