"""

---> Most Stones Removed with Same Row or Column
---> Medium

"""
from collections import defaultdict


class Solution:
    def removeStones(self, stones) -> int:
        def dfs(stone_pos):
            nonlocal count
            visited[(stone_pos[0], stone_pos[1])] = True

            for c in col_stones[stone_pos[0]]:
                if not visited[c[0], c[1]]:
                    dfs(c)
                    count += 1

            for r in row_stones[stone_pos[1]]:
                if not visited[r[0], r[1]]:
                    dfs(r)
                    count += 1

        visited = {}
        col_stones = defaultdict(list)
        row_stones = defaultdict(list)
        count = 0

        for s in stones:
            visited[(s[0], s[1])] = False
            col_stones[s[0]].append(s)
            row_stones[s[1]].append(s)

        for s in stones:
            if not visited[(s[0], s[1])]:
                dfs(s)

        return count

    def removeStones_sol2(self, stones) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count

            px, py = find(x), find(y)
            if px == py:
                return

            elif px > py:
                parent[px] = py

            else:
                parent[py] = px

            count += 1

        n = len(stones)
        parent = [i for i in range(n)]
        count = 0
        rows = {}
        cols = {}

        for i, (r, c) in enumerate(stones):
            if r not in rows:
                rows[r] = i
            else:
                union(rows[r], i)

            if c not in cols:
                cols[c] = i
            else:
                union(cols[c], i)
        print(parent)
        return count


in_stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
a = Solution()
# print(a.removeStones(in_stones))
print(a.removeStones_sol2(in_stones))


"""

Approach 1:
DFS
Add all the stones to their respective row or column, then check if the particular row or column has more than 1 stone, 
if their are increase the count
Reference - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/1578584/Python-dfs

Approach 2:
Union Find
Put stones in a their row and column and assign same values to stones in the same row or column, Increase the count if 
the parent of any 2 stones are same
Reference - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/1501637/Python-Union-Find-faster-than-100

"""
