"""

---> Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
---> Medium

"""
from collections import deque


class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0
        while r < len(nums):
            while min_deque and nums[r] <= nums[min_deque[-1]]:
                print("min", nums[r], nums[min_deque[-1]])
                min_deque.pop()
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                print("max", nums[r], nums[max_deque[-1]])
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()

            ans = max(ans, r - l + 1)
            r += 1
            print(min_deque, max_deque)
        return ans
    
    
in_nums = [10, 1, 2, 4, 7, 2]
in_limit = 5
a = Solution()
print(a.longestSubarray(in_nums, in_limit))


"""
Reference - 

"""
