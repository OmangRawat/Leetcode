"""

---> Merge Sorted Array
---> Medium

"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = n + m - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
        return nums1


in_m = 3
in_n = 3
in_nums1 = [1, 2, 3, 0, 0, 0]
in_nums2 = [2, 5, 6]
a = Solution()
print(a.merge(in_nums1, in_m, in_nums2, in_n))
