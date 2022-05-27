"""

---> Increasing Subsequences
---> Medium

"""


class Solution:
    def findSubsequences(self, nums):
        def dfs(curr_nums):
            if len(current) >= 2 and current not in ans:
                ans.append(current.copy())
            # visited = set()
            for i in range(len(curr_nums)):
                num = curr_nums[i]
                if current and num < current[-1]:
                    continue
                # if num not in visited:
                current.append(num)
                dfs(curr_nums[i + 1:])
                current.pop()

        ans = []
        current = []
        dfs(nums)
        return ans


in_nums = [4, 6, 7, 7]
a = Solution()
print(a.findSubsequences(in_nums))

"""
"""
