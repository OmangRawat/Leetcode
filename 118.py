"""

---> Pascal's Triangle
---> Easy

"""


class Solution:
    def generate(self, numRows: int):
        ans = [[1]]

        for _ in range(numRows - 1):
            last_iter = ans[-1].copy()
            next_iter = [1]
            for i in range(len(last_iter) - 1):
                next_iter.append(last_iter[i] + last_iter[i + 1])
            next_iter.append(1)
            ans.append(next_iter)

        return ans


in_row = 5
a = Solution()
print(a.generate(in_row))
