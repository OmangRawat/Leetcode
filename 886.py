"""

---> Possible Bipartition
---> Medium

"""
from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        if not dislikes:
            return True

        queue, visited = deque(), {}
        dislike_graph = defaultdict(set)

        for p1, p2 in dislikes:
            dislike_graph[p1].add(p2)
            dislike_graph[p2].add(p1)

        for i in range(1, n + 1):
            if i not in visited:
                queue.append(i)
                visited[i] = 0 if i - 1 in visited and visited[i - 1] == 1 else 1

            while queue:
                curr_person = queue.popleft()
                for p1 in dislike_graph[curr_person]:
                    if p1 not in visited:
                        queue.append(p1)
                        visited[p1] = 1 if visited[curr_person] == 0 else 0
                    else:
                        if visited[p1] == visited[curr_person]:
                            return False
        return True

    def possibleBipartition_sol2(self, n: int, dislikes) -> bool:
        def dfs(cur, g):
            nonlocal group

            if cur in group:
                return group[cur] == g

            group[cur] = g
            curr_dislikes = dislike_graph.get(cur, [])

            for n1 in curr_dislikes:
                if not dfs(n1, -g):
                    return False

            return True

        dislike_graph = defaultdict(list)

        for p1, p2 in dislikes:
            dislike_graph[p1].append(p2)
            dislike_graph[p2].append(p1)

        group = {}

        for i in range(1, n + 1):
            if not dfs(i, group.get(i, 1)):
                return False
        return True


in_n = 4
in_dislikes = [[1, 2], [1, 3], [2, 4]]
a = Solution()
print(a.possibleBipartition(in_n, in_dislikes))
print(a.possibleBipartition_sol2(in_n, in_dislikes))


"""
Reference - https://leetcode.com/problems/possible-bipartition/discuss/1416469/Python-Clean-and-Simple-BFS-solution


Reference - https://leetcode.com/problems/possible-bipartition/discuss/1591450/Python-DFS-or-assign-group
"""
