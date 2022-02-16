"""

---> Unique Binary Search Trees
---> Medium

"""
from functools import lru_cache
from math import factorial


class Solution:
    @lru_cache
    def numTrees(self, n: int) -> int:
        # Memoization (@cache is imp without it it is just simple recursive solution)
        if n <= 1:
            return 1
        return sum(self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n + 1))

    def numTrees_sol2(self, n: int) -> int:
        # Tabulation
        unique_bst = [0] * (n + 1)
        unique_bst[0], unique_bst[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                unique_bst[i] += unique_bst[j - 1] * unique_bst[i - j]
        return unique_bst[n]

    def numTrees_sol3(self, n: int) -> int:
        # Catalan Numbers (can be used to solve many recursive problems)
        return factorial(2*n) // (factorial(n)*factorial(n+1))


in_n = 3
a = Solution()
print(a.numTrees(in_n))
print(a.numTrees_sol2(in_n))
print(a.numTrees_sol3(in_n))


"""
Reference - https://leetcode.com/problems/unique-binary-search-trees/discuss/1565543/C%2B%2BPython-5-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Catalan-O(N)

Approach 1 and 2:
Unique Bst of n node tree is keep a node at root and divide the remaining into 2 parts of i - 1 node and n - i nodes
So the result is no. of ways you can make a unique BST of i - 1 nodes on left into n - i nodes on right

Approach 2:
The series it denotes is similar to Catalan Numbers series which is used in many recursive problems

"""
