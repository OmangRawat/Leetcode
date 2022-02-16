"""

---> Find Eventual Safe States
---> Medium

"""
from collections import deque, Counter, defaultdict


class Solution:
    def eventualSafeNodes(self, graph):
        # Kahn's Algorithm
        queue = deque()
        visited = set()

        neighbour_count = Counter()

        neighbor_table = defaultdict(list)

        for i, neighbors in enumerate(graph):
            neighbour_count[i] = len(neighbors)

            for n in neighbors:
                neighbor_table[n].append(i)

            if len(neighbors) == 0:
                queue.append(i)
                visited.add(i)

        safe_nodes = []

        while queue:
            curr = queue.popleft()
            safe_nodes.append(curr)

            for neighbor in neighbor_table[curr]:
                neighbour_count[neighbor] -= 1

                if neighbor not in visited and neighbour_count[neighbor] == 0:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return sorted(safe_nodes)

    def eventualSafeNodes_sol2(self, graph):
        # DFS
        def dfs(node):
            if node in safe_nodes:
                return safe_nodes[node]
            safe_nodes[node] = False   # For self-loops

            safe_nodes[node] = all(dfs(v) for v in graph[node])
            return safe_nodes[node]

        safe_nodes = {}
        return [i for i in range(len(graph)) if dfs(i)]


in_graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
a = Solution()
print(a.eventualSafeNodes(in_graph))
print(a.eventualSafeNodes_sol2(in_graph))


"""

Approach 1:
Kahn's Algorithm
Keep track of number of edges going out from the node
Find the terminal states and append to neighbor table the nodes from which they have edges coming in, The one which 
don't have any edges coming are terminal nodes and they are also safe nodes. Subtract the number of edges for each 
terminal node connected to the all the nodes, if after removing all terminal nodes there are 0 edges left then it is a 
safe node

Reference - https://leetcode.com/problems/find-eventual-safe-states/discuss/1604866/Python3-Kahn's-Algorithm-(count-number-of-reach-times)-with-BFS

Approach 2:
DFS
Check for all the edges starting from the node, if they are to terminal nodes then return True, if all the edges return 
true it is a safe node

Reference - https://leetcode.com/problems/find-eventual-safe-states/discuss/1538114/Python-oror-Extremely-simple-DFS-solution

"""
