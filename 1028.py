"""

---> Recover a Tree From Preorder Traversal
---> Hard

"""
from tree_func import *


class Solution:
    def recoverFromPreorder(self, traversal: str):
        n = len(traversal)
        root = Node(None)
        level = 0
        char = ""
        stack = [(root, -1, root.value)]
        for index in range(n):
            print(stack)
            if traversal[index] == "-":
                level += 1
            else:
                char += traversal[index]
            if index == n - 1 or (traversal[index].isnumeric() and traversal[index + 1] == "-"):
                while stack[-1][1] > level:
                    stack.pop()
                node = Node(char)
                if stack[-1][1] == level:
                    stack.pop()
                    stack[-1][0].right = node
                else:
                    stack[-1][0].left = node
                stack.append((node, level, node.value))
                char = ""
                level = 0
        return root.left


in_traversal = "1-2--3---4-5--6---7"
# in_traversal = "10-7--8"
a = Solution()
pretty_print(a.recoverFromPreorder(in_traversal))
