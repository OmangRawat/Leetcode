"""

---> Find All People With Secret
---> Hard

"""
from collections import defaultdict


class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        def union(a, b):
            p_a, p_b = find(a), find(b)
            if p_a == firstPerson:
                parent[b] = firstPerson
            elif p_b == firstPerson:
                parent[a] = firstPerson
            elif p_a < p_b:
                parent[b] = p_a
            else:
                parent[a] = p_b

        def find(a):
            if parent[a] != a:
                return find(parent[a])
            return a

        parent = [x for x in range(n)]
        time_dict = defaultdict(list)

        for p1, p2. t in meetings:
            time_dict[t].append((p1, p2))

        for p1, p2 in sorted(meetings.items()):
            union(p1, p2)
