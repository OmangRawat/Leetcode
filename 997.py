"""

---> Find the Town Judge
---> Easy

"""
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust) -> int:
        trust_record = [0] * (n + 1)
        for person1, person2 in trust:
            trust_record[person1] -= 1
            trust_record[person2] += 1
        return next((i for i in range(1, n + 1) if trust_record[i] == n - 1), -1)

    def findJudge_sol2(self, n: int, trust) -> int:
        trust_given = defaultdict(int)
        trust_received = defaultdict(int)

        for relationship in trust:
            trust_given[relationship[1]] += 1
            trust_received[relationship[0]] += 1

        for key in range(1, n + 1):
            if not trust_received[key] and trust_given[key] == n - 1:
                return key

        return -1


in_n = 3
in_trust = [[1, 3], [2, 3], [3, 1]]
a = Solution()
print(a.findJudge(in_n, in_trust))
print(a.findJudge_sol2(in_n, in_trust))


"""

Approach 1:
Keep track of (trust received -  trust given) for each person and judge would be the one with that equal to (n - 1)

Reference - https://leetcode.com/problems/find-the-town-judge/discuss/1621150/O(n)-solution-in-Python

Approach 2:
Keep 2 dict with trust given and trust received dict and check for the key if it has 0 given and n - 1 received

Reference - https://leetcode.com/problems/find-the-town-judge/discuss/1624781/python-O(n)-2-Hashmaps-(dicts)

"""
