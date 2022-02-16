"""

---> Smallest Range II
---> Medium

"""


class Solution:
    def smallestRangeII(self, nums, k: int) -> int:
        nums.sort()
        min_number, max_number = nums[0], nums[-1]
        ans = max_number - min_number
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                max_number = max(nums[-1] - k, nums[i] + k)
                min_number = min(nums[0] + k, nums[i + 1] - k)
                ans = min(ans, max_number - min_number)

        return ans


in_nums = [1, 3, 6]
in_k = 3
a = Solution()
print(a.smallestRangeII(in_nums, in_k))


"""

Smallest difference between max and min would be when the difference between smaller of the 2 + k and larger of the 
2 - k is taken
Reference - https://leetcode.com/problems/smallest-range-ii/discuss/1549843/python-well-commented-easy-to-understand-and-follow-O(nlogn)

Complexities:
Time -> O(NlogN)
Space -> O(1)

"""