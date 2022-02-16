"""

---> Maximum Sum Circular Sub-array
---> Medium

"""


class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        # Variation of Kadane's Algo
        total, max_sum, cur_max, min_sum, cur_min = 0, nums[0], 0, nums[0], 0
        for i in nums:
            cur_max = max(cur_max + i, i)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + i, i)
            min_sum = min(min_sum, cur_min)
            total += i
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


in_nums = [3, -2, 2, -3]
a = Solution()
print(a.maxSubarraySumCircular(in_nums))


"""

Approach 1:
Can be divided into 3 cases:
Explained properly in reference
Reference - https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass

Complexities:
Time -> O(N)
Space -> O(1)

Approach 2:
Using Queue or Heap
Reference - https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/1348545/Python-3-solutions-Clean-and-Concise-O(1)-Space

Complexities:
Time -> O(N) for queue and O(NlogN) for heap
Space -> O(N)

"""

