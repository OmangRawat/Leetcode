"""

---> Number of Provinces
---> Medium

"""


class Solution:
    def findCircleNum(self, isConnected) -> int:
        def dfs(city1):
            if visited[city1] == 0:
                visited[city1] = 1
                for city2 in range(len(isConnected)):
                    if visited[city2] == 0 and isConnected[city1][city2] == 1:
                        dfs(city2)

        visited = [0] * len(isConnected)
        ans = 0
        for i in range(len(isConnected)):
            if visited[i] == 0:
                dfs(i)
                ans += 1
        return ans


in_isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
a = Solution()
print(a.findCircleNum(in_isConnected))


"""
Reference - https://leetcode.com/problems/number-of-provinces/discuss/1647819/Python3-DFS-Solution-Faster-Than-93.33
"""
