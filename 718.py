"""

---> Maximum Length of Repeated Subarray
---> Medium

"""


class Solution:
    def findLength(self, nums1, nums2) -> int:
        n = len(nums1)
        m = len(nums2)
        # t = [[0 for i in range(m + 1)] for j in range(n + 1)]
        curr_arr = [0 for _ in range(m + 1)]
        # next_arr = [0 for _ in range(m + 1)]
        last_len = 0
        ans = 0
        for i in range(1, n + 1):
            # for j in range(1, m + 1):
            #     if nums1[i - 1] == nums2[j - 1]:
            #         # t[i][j] = 1 + t[i - 1][j - 1]
            #         next_arr[j] = curr_arr[j - 1] + 1
            #         # last_len += 1
            #         ans = max(ans, next_arr[j])
            #     else:
            #         # t[i][j] = 0
            #         last_len = 0
            #     # ans = max(ans, t[i][j])
            #     # next_arr = [int(i + 1) for i in ]
            #     print(curr_arr, next_arr)
            #     print(nums1[i - 1], nums2[j - 1], next_arr[j])
            next_arr = [int(curr_arr[j - 1] + 1) if (nums1[i - 1] == nums2[j - 1] or j != 0) else 0 for j in range(0, m + 1)]
            print(nums1[i - 1], curr_arr, next_arr)
            curr_arr = next_arr
            ans = max(ans, max(curr_arr))
        return ans


in_nums1 = [1, 2, 3, 2, 1]
in_nums2 = [3, 2, 1, 4, 7]
a = Solution()
print(a.findLength(in_nums1, in_nums2))
