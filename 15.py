"""

---> 3Sum
---> Medium

"""


class Solution:
    def threeSum(self, nums):
        l = len(nums)
        nums.sort()
        ans = []
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = l - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return ans


in_nums = [-1, 0, 1, 2, -1, -4]
a = Solution()
print(a.threeSum(in_nums))
