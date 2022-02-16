"""

---> Search a 2D Matrix
---> Medium

"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        array = []
        for row in matrix:
            array += row

        low, high = 0, len(array) - 1

        while low < high:
            mid = (low + high) // 2
            if array[mid] == target:
                return True
            elif target > array[mid]:
                low = mid + 1
            else:
                high = mid

        return array[low] == target


in_matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
in_target = 3
a = Solution()
print(a.searchMatrix(in_matrix, in_target))
