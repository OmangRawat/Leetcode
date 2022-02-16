"""

---> Matchsticks to Square
---> Medium

"""


class Solution:
    def makesquare(self, matchsticks) -> bool:
        def check_for_matchstick(i):
            if i == len(matchsticks):
                # return not any(size)
                return True

            for j in range(4):
                if size[j]:
                    if size[j] - matchsticks[i] >= 0:
                        size[j] = size[j] - matchsticks[i]
                        print(i, j, size)

                        if check_for_matchstick(i + 1):
                            return True

                        size[j] += matchsticks[i]

            return False

        target = sum(matchsticks)

        if target % 4 != 0:
            return False

        target = target // 4

        size = [target] * 4
        matchsticks.sort(reverse=True)

        return check_for_matchstick(0)


in_matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# in_matchsticks = [1, 1, 2, 2, 2]
# in_matchsticks = [3, 3, 3, 3, 4]
a = Solution()
print(a.makesquare(in_matchsticks))


"""
"""
