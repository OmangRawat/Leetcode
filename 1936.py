"""

---> Add Minimum Number of Rungs
---> Medium

"""


class Solution:
    def addRungs(self, rungs, dist: int) -> int:
        n = len(rungs)
        ans = 0
        last_rung = 0

        for i in range(n):
            if rungs[i] - last_rung > dist:
                distance_between = rungs[i] - last_rung - 1
                ans += distance_between // dist
                # ans += rungs_needed - 1 if distance_between % dist == 0 else rungs_needed

            last_rung = rungs[i]

        return ans

    def addRungs_sol2(self, rungs, dist: int) -> int:
        return sum((rungs[i] - (rungs[i - 1] if i else 0) - 1) // dist for i in range(len(rungs)))


in_rung = [1, 3, 5, 10]
in_dist = 2
a = Solution()
print(a.addRungs(in_rung, in_dist))
print(a.addRungs_sol2(in_rung, in_dist))


"""
Difference between the consecutive rung - 1 then divide it by difference and that will give no of more rungs needed 
between any two rungs so that it can climb up to next rung
Reference - https://leetcode.com/problems/add-minimum-number-of-rungs/discuss/1633254/python3%3A-time-O(n)
"""
