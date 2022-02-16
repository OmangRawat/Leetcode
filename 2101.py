"""

---> Detonate the Maximum Bombs
---> Medium

"""
from collections import defaultdict
from copy import deepcopy


class Solution:
    def maximumDetonation(self, bombs) -> int:
        number_of_bombs = len(bombs)
        can_detonate = defaultdict(set)

        for i in range(number_of_bombs - 1):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, number_of_bombs):
                x2, y2, r2 = bombs[j]
                dist2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if r1 ** 2 >= dist2:
                    can_detonate[i].add(j)
                if r2 ** 2 >= dist2:
                    can_detonate[j].add(i)

        final_can_detonate = defaultdict(set)
        while final_can_detonate != can_detonate:
            final_can_detonate = deepcopy(can_detonate)
            for k in final_can_detonate:
                for v in final_can_detonate[k]:
                    can_detonate[k].update(can_detonate[v] - {k})

        return (max(len(can_detonate[k]) for k in can_detonate) if can_detonate else 0) + 1

    def maximumDetonation_sol2(self, bombs) -> int:
        number_of_bombs = len(bombs)
        g = [[] for i in range(number_of_bombs)]
        visited = [None] * number_of_bombs

        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2:
                    g[i] += [j]

        def dft(node):
            nonlocal visited, v
            for child in g[node]:
                if ~(v >> child) & 1:
                    if visited[child]:
                        v |= visited[child]
                    else:
                        v |= (1 << child)
                        dft(child)

        bombs_will_detonate = 0
        for i in range(number_of_bombs):
            v = 1 << i
            dft(i)
            bombs_will_detonate = max(bombs_will_detonate, bin(v).count('1'))
            visited[i] = v
        return bombs_will_detonate


in_bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
a = Solution()
print(a.maximumDetonation(in_bombs))


"""

Approach 1:
For every pair of bombs check if it detonates because of any of the twp and add in the list of bombs getting detonated 
because of that bomb. Add the list of bombs detonating because of the bombs that detonate because of the main bomb


Approach 2:
No idea

Reference - https://leetcode.com/problems/detonate-the-maximum-bombs/discuss/1640128/Python3-BFS%3A-keep-updating-until-there-is-no-change
"""
