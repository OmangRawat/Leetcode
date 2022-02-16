"""

---> Rotate Image
---> Medium

"""


class Solution:
    def rotate(self, matrix):
        def get_new_positions(size, a, b):
            return b, size - a - 1
        n = len(matrix)
        if n <= 1:
            return
        for i in range(n+1//2):
            for j in range(i, n - i - 1):
                changed_i = i
                changed_j = j
                val = matrix[i][j]
                for _ in range(4):
                    changed_i, changed_j = get_new_positions(n, changed_i, changed_j)
                    temp_val = matrix[changed_i][changed_j]
                    matrix[changed_i][changed_j] = val
                    val = temp_val
                    # print(changed_i, changed_j)
                    # print(matrix)


in_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = Solution()
a.rotate(in_matrix)
print(in_matrix)


"""

Layers is like Outer square then inner and so on (the one made by a is one layer)
    a a a
    a A a
    a a a
int((n+1)/2) layers in total need to be rotated (first layer is 0th)
n - 1 - 2*i nodes in ith outer layer

Reference: https://leetcode.com/problems/rotate-image/discuss/367514/python-beats-96-with-Image-helps-u-understand

Complexities:
Time ->  O(N^2)
Space -> 

"""
