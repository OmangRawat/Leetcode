"""

---> Valid Triangle Number
---> Medium

"""
from bisect import bisect_right


class Solution:
    def triangleNumber(self, nums) -> int:
        ans = 0
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1

        return ans

    def triangleNumber_sol2(self, nums) -> int:
        nums.sort()
        n, ans = len(nums), 0

        for num1 in range(n - 2):
            num3 = num1 + 2
            for num2 in range(num1 + 1, n - 1):
                max_side = nums[num1] + nums[num2] - 1

                if max_side < nums[num2]:
                    break

                num3 = bisect_right(nums, max_side, num3)
                ans += min(num3, n) - (num2 + 1)

        return ans


in_nums = [4, 2, 3, 4]
a = Solution()
print(a.triangleNumber(in_nums))
print(a.triangleNumber_sol2(in_nums))


"""
Approach 1:
Fix the max number then find 2 numbers smaller than that that would have sum greater than the number that we chose
(right - left) gives numbers because if the number left with right has sum greater than the max one then all numbers 
between left nd right would do so to if replacing left with them

Approach 2:
Fix the smallest number then choose 1 number and sum it to get the max length of the third siide that is possible, 
check where it lies in the array
min(num3, n) - (num2 + 1) will give all the numbers keeping smallest and max side fixed

"""
