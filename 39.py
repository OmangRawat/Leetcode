"""

---> Combination Sum
---> Medium

"""


class Solution:
    def combinationSum(self, candidates, target: int):
        def check_sum(nums, curr_target, path):
            if curr_target < 0:
                return
            if curr_target == 0:
                ans.append(path)

            for i in range(len(nums)):
                check_sum(nums[i:], curr_target - nums[i], path + [nums[i]])

        ans = []
        combination = []
        check_sum(candidates, target, combination)
        return ans


in_candidates = [2, 3, 6, 7]
in_target = 7
a = Solution()
print(a.combinationSum(in_candidates, in_target))
