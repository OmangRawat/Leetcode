"""

---> Number of Operations to Make Network Connected
---> Medium

"""


class Solution:
    def makeConnected(self, n: int, connections) -> int:
        # Union Find
        def find_root(comp):
            while comp != parent[comp]:
                parent[comp] = parent[parent[comp]]
                comp = parent[comp]
            return comp

        disconnected_components = n

        if len(connections) < n - 1:
            return -1

        parent = [i for i in range(n)]

        for comp1, comp2 in connections:
            root1 = find_root(comp1)
            root2 = find_root(comp2)
            if root1 != root2:
                parent[root1] = root2
                disconnected_components -= 1

        return disconnected_components - 1


in_n = 6
in_connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
a = Solution()
print(a.makeConnected(in_n, in_connections))


"""

Approach:
Start by taking all the components to be disconnected, for every one connection remove one disconnected component
Return disconnected components  - 1 because it takes n - 1 connections to connect n disconnected components

Reference - https://leetcode.com/problems/number-of-operations-to-make-network-connected/discuss/1631752/Python-Union-Find-solution-with-Comments-Explanation
"""
