"""

---> Combination Sum II
---> Medium

"""


class Solution:
    def combinationSum2(self, candidates, target: int):
        def check_sum(curr_nums, curr_target, curr_combination):
            curr_nums.sort()
            if curr_target < 0:
                return

            if curr_target == 0:
                ans.append(curr_combination)

            for i in range(len(curr_nums)):
                if i > 0 and curr_nums[i] == curr_nums[i - 1]:
                    continue
                check_sum(curr_nums[i + 1:], curr_target - curr_nums[i], curr_combination + [curr_nums[i]])

        ans = []
        combination = []
        check_sum(candidates, target, combination)
        return ans


in_candidates = [10, 1, 2, 7, 6, 1, 5]
in_target = 8
a = Solution()
print(a.combinationSum2(in_candidates, in_target))
