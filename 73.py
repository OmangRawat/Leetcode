"""

---> Set Matrix Zeroes
---> Medium

"""


class Solution:
    def setZeroes(self, matrix) -> None:
        rows, columns = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0

        return matrix


in_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
a = Solution()
print(a.setZeroes(in_matrix))
