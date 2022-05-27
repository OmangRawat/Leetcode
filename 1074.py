"""

--->  Number of Submatrices That Sum to Target
---> Hard

"""
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        def count_sub_array_target(nums):
            sub_ans = 0
            cur_sum = 0
            seen = defaultdict(int)
            seen[0] = 1

            for j in range(len(nums)):
                cur_sum += nums[j]

                if cur_sum - target in seen:
                    sub_ans += seen[cur_sum - target]
                seen[cur_sum] += 1

            return sub_ans

        m, n = len(matrix), len(matrix[0])
        prefix_sum_y = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                prefix_sum_y[i][j] += matrix[i][j] + (prefix_sum_y[i][j - 1] if j - 1 >= 0 else 0)

        ans = 0
        print(prefix_sum_y)
        for y1 in range(n):
            for y2 in range(y1, n):

                rows = []
                for x in range(m):
                    block = prefix_sum_y[x][y2] - (prefix_sum_y[x][y1 - 1] if y1 - 1 >= 0 else 0)
                    rows.append(block)

                temp_ans = count_sub_array_target(rows)
                ans += temp_ans
                print(prefix_sum_y)
        return ans


in_matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
in_target = 0
a = Solution()
print(a.numSubmatrixSumTarget(in_matrix, in_target))


"""



"""
