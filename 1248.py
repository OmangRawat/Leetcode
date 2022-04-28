"""

---> Count Number of Nice Subarrays
---> Medium

"""


class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        odd_no_count, odd_idx, ans = 0, [], 0
        for i in range(len(nums)):
            if nums[i] % 2:
                odd_no_count += 1
                odd_idx.append(i)
            if odd_no_count >= k:
                if odd_no_count == k:
                    ans += odd_idx[odd_no_count - k] + 1
                else:
                    ans += odd_idx[odd_no_count - k] - odd_idx[odd_no_count - k - 1]

        return ans


in_nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
in_k = 2
a = Solution()
print(a.numberOfSubarrays(in_nums, in_k))


"""

Approach:
Keep track of all odd indexes
For no. of odds equal to k there will be no. of sub-arrays equal to index + 1
For no. of odds greater than k there will be no. between indexes of odd index k and k + 1 before current one

Another Approach:
Track k odd numbers using 2 pointers of sliding window 

"""
