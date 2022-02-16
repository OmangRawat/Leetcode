"""

---> Satisfiability of Equality Equations
---> Medium

"""
from collections import defaultdict


class Solution:
    def equationsPossible(self, equations) -> bool:
        connections = {chr(num): chr(num) for num in range(ord("a"), ord("z") + 1)}

        def check(val):
            if connections[val] == val:
                return val
            connections[val] = check(connections[val])
            return connections[val]

        for x, sign, _, y in equations:
            if sign == "=":
                parent_x, parent_y = check(x), check(y)
                connections[parent_x] = parent_y
        print(connections)
        for x, sign, _, y in equations:
            if sign == "!" and check(x) == check(y):
                return False

        return True

    def equationsPossible_sol2(self, equations) -> bool:
        def isConnected(var1, var2):
            stack, visited = [var1], set()
            while stack:
                curr = stack.pop()
                if curr == var2:
                    return True
                if curr not in visited:
                    visited.add(curr)
                    for connection in graph[curr]:
                        if connection not in visited:
                            stack.append(connection)
            return False

        graph, not_equal = defaultdict(list), []

        for x, sign, _, y in equations:
            if sign == "!":
                not_equal.append((x, y))
            if sign == "=" and x != y:
                graph[x].append(y)
                graph[y].append(x)

        for x, y in not_equal:
            if x == y or isConnected(x, y):
                return False
        return True


in_equations = ["b==a", "a==b"]
a = Solution()
print(a.equationsPossible(in_equations))
# print(a.equationsPossible_sol2(in_equations))


"""

Approach 1:
# Union Find
Make all connections using the == equations by giving all equal elements to one parent and then check if any != equation 
violates the connections made using them 

Approach 2:
# DFS
Same make all the connections and keep track of the visited ones and check for the ones that have not been visited

Reference - https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/1582134/Python-2-Methods-DFS-and-Union-Find
"""
