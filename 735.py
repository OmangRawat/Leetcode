"""

---> Asteroid Collision
---> Medium

"""


class Solution:
    def asteroidCollision(self, asteroids):
        ans = []
        for asteroid in asteroids:
            while len(ans) and asteroid < 0 and ans[-1] > 0:
                if ans[-1] == -asteroid:
                    ans.pop()
                    break
                elif ans[-1] < -asteroid:
                    ans.pop()
                elif ans[-1] > -asteroid:
                    break
            else:
                ans.append(asteroid)
        return ans


in_asteroids = [5, 10, -5]
a = Solution()
print(a.asteroidCollision(in_asteroids))


"""

Reference - https://leetcode.com/problems/asteroid-collision/discuss/109666/Python-O(n)-Stack-based-with-explanation

Complexities:
Time -> O(N^2)
Space -> O(N)

"""
