"""

---> 4Sum
---> Medium

"""


class Solution:
    def fourSum(self, nums, target: int):
        def twoSum(target_left, num1_index, num2_index, start_index):
            dictionary = {}
            visited = set()
            for i in range(start_index, len(nums)):
                if nums[i] in dictionary:
                    if (nums[dictionary[nums[i]]], nums[i]) not in visited:
                        ans.append([nums[num1_index], nums[num2_index], nums[dictionary[nums[i]]], nums[i]])
                        visited.add((nums[dictionary[nums[i]]], nums[i]))
                else:
                    dictionary[target_left - nums[i]] = i

        nums.sort()
        ans = []
        for num1 in range(len(nums)):
            if num1 != 0 and nums[num1] == nums[num1 - 1]:
                continue

            for num2 in range(num1 + 1, len(nums)):
                if num2 != num1 + 1 and nums[num2] == nums[num2 - 1]:
                    continue
                twoSum(target - (nums[num1] + nums[num2]), num1, num2, num2 + 1)

        return ans


in_nums = [1, 0, -1, 0, -2, 2]
in_target = 0
a = Solution()
print(a.fourSum(in_nums, in_target))
