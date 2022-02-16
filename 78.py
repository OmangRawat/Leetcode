"""

---> Subsets
---> Medium

"""


class Solution:
    def subsets(self, nums):
        ans = []
        n = len(nums)

        for subset_length in range(2**n):
            curr_list = []
            for index in range(n):
                if subset_length & (2**index):
                    curr_list.append(nums[index])
            ans.append(curr_list)
        return ans

    def subsets_sol2(self, nums):
        def dfs(curr_nums):
            power_set.append(curr_set.copy())
            for index, value in enumerate(curr_nums):
                curr_set.append(value)
                dfs(curr_nums[index + 1:])
                curr_set.pop()
            return power_set

        curr_set = []
        power_set = []
        return dfs(nums)


in_nums = [1, 2, 3]
a = Solution()
print(a.subsets(in_nums))
print(a.subsets_sol2(in_nums))
