"""

---> All Paths From Source to Target
---> Medium

"""
from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(node, path):
            if node == target:
                ans.append(path)
                return

            for neighbour in paths[node]:
                dfs(neighbour, path + [neighbour])

        paths = defaultdict(set)
        for i, nodes in enumerate(graph):
            for node in nodes:
                paths[i].add(node)

        target = len(graph) - 1
        ans = []

        dfs(0, [0])
        return ans

    def allPathsSourceTarget_sol2(self, graph):
        def walk(path):
            if path[-1] == target:
                ans.append(path.copy())
                return None

            for i in graph[path[-1]]:
                path.append(i)
                walk(path)
                path.pop()

        target = len(graph) - 1
        ans = []
        walk([0])
        return ans


in_graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
a = Solution()
print(a.allPathsSourceTarget(in_graph))
print(a.allPathsSourceTarget_sol2(in_graph))


"""

Approach 1:
Reference - https://leetcode.com/problems/all-paths-from-source-to-target/discuss/1644548/python-very-simple-clean-dfs-solution-beats-90


Approach 2:
Backtracking
Reference - https://leetcode.com/problems/all-paths-from-source-to-target/discuss/1636892/Python-backtracking
"""
