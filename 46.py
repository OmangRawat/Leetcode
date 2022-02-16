"""

---> Permutations
---> Medium

"""
from itertools import permutations


class Solution:
    def permute(self, nums):
        patterns = list(permutations(nums, len(nums)))
        return [list(x) for x in patterns]

    def permute_sol2(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        ans = []

        for i in range(len(nums)):
            rem_pattern = self.permute_sol2(nums[:i] + nums[i + 1:])

            for j in rem_pattern:
                ans.append([nums[i]] + j)

        return ans


in_nums = [1, 2, 3]
a = Solution()
print(a.permute(in_nums))
print(a.permute_sol2(in_nums))


"""

Approach 1:
Simply use permutation func in itertools module of python

Approach 2: 
Keep one digit outside and then check permutations of the left numbers in the array, recursively do it unless length of 
the digit left in the array is 1 then return the array with the number as their would be only on permutation

Reference - https://leetcode.com/problems/permutations/discuss/1660043/Python-or-Backtracking

"""
