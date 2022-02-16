"""

---> Shortest Unsorted Continuous Subarray
---> Medium

"""
import math


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        stack = []
        left, right = len(nums), 0
        for i in range(len(nums)):
            while len(stack) > 0 and nums[i] < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)

        stack.clear()
        for j in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[j] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(j)

        return right - left + 1 if right > left else 0

    def findUnsortedSubarray_sol2(self, nums) -> int:
        low, high = math.inf, -math.inf

        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                low = min(low, nums[i])

        flag = False
        for j in range(len(nums) - 2, -1, -1):
            if nums[j] > nums[j + 1]:
                flag = True
            if flag:
                high = max(high, nums[j])

        i, j = 0, len(nums) - 1
        for i in range(len(nums)):
            if low < nums[i]:
                break
        for j in range(len(nums) - 1, -1, -1):
            if high > nums[j]:
                break

        return j - i + 1 if j > i else 0


in_nums = [2, 6, 4, 8, 10, 9, 15]
a = Solution()
# print(a.findUnsortedSubarray(in_nums))
print(a.findUnsortedSubarray_sol2(in_nums))


"""

Find least index after which their is a number greater and max index before which their is a larger number

Approach 1:

Complexities:
Time -> O(N)
Space -> O(N)

Approach 2:

Complexities:
Time -> O(N)
Space -> O(1)
 
"""
