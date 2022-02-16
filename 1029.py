"""

---> Two City Scheduling
---> Medium

"""


class Solution:
    def twoCitySchedCost(self, costs) -> int:
        ans = 0
        n = len(costs)
        for i in range(n):
            costs[i][1] -= costs[i][0]
            ans += costs[i][0]
            costs[i][0] = 0

        costs.sort(key=lambda x: x[1])

        for i in range(n // 2):
            ans += costs[i][1]
        return ans


in_costs = [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]
a = Solution()
print(a.twoCitySchedCost(in_costs))


"""

Change the array to send all the people to city A first then check which n/2 people would be best to send to city B i.e 
would take the minimum cost to send to B and not A

"""
