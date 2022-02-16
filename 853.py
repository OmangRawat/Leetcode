"""

---> Car Fleet
---> Medium

"""
import collections


class Solution:
    def carFleet(self, target, position, speed) -> int:
        stack = collections.deque([(s, p) for s, p in sorted(zip(position, speed))])
        count = 1
        p, s = stack.pop()
        time = (target - p) / float(s)
        while stack:
            if time >= (target - stack[-1][0]) / float(stack[-1][1]):
                stack.pop()
            else:
                count += 1
                p, s = stack.pop()
                time = (target - p) / float(s)
        return count

    def carFleet_sol2(self, target, position, speed) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        ans, cur_min = 0, 0
        for t in time[::-1]:
            if t > cur_min:
                ans += 1
                cur_min = t
        return ans


in_target = 12
in_position = [10, 8, 0, 5, 3]
in_speed = [2, 4, 1, 1, 3]
a = Solution()
# print(a.carFleet(in_target, in_position, in_speed))
print(a.carFleet_sol2(in_target, in_position, in_speed))


"""

A car that would normally reach faster than the car in a position before it will be part of the that fleet
Approach 1:
Reference - https://leetcode.com/problems/car-fleet/discuss/1537985/Python3-Increasing-stack

Complexities:
Time -> 
Space -> 


Approach 2:
Reference - https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward

Complexities:
Time -> O(NlogN)
Space -> O(N)

"""
