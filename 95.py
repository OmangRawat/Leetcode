"""

---> Unique Binary Search Trees II
---> Medium

"""
from tree_func import *


class Solution:
    def generateTrees(self, n: int):
        def dp(values):
            if not values:
                yield None
            for index, root in enumerate(values):
                for left in dp(values[:index]):
                    for right in dp(values[index + 1:]):
                        yield Node(root, left, right)

        return dp(list(range(1, n + 1)))


in_n = 5
a = Solution()
for i in a.generateTrees(in_n):
    pretty_print(i)


"""

To get all the permutations, choose a root, choose the left element from elements smaller than root and a right element 
from elements greater than root

"""
