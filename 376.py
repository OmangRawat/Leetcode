"""

---> Wiggle Subsequence
---> Medium

"""


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        final_nums = [nums[0]]
        for i in range(1, n):
            if i == 1 or len(final_nums) == 1:
                if nums[i] > final_nums[0] or nums[i] < final_nums[0]:
                    final_nums.append(nums[i])
                else:
                    pass
            else:
                if nums[i] > final_nums[-1]:
                    if final_nums[-1] >= final_nums[-2]:
                        final_nums[-1] = nums[i]
                    else:
                        final_nums.append(nums[i])
                else:
                    if nums[i] == final_nums[-1]:
                        continue
                    if final_nums[-1] <= final_nums[-2]:
                        final_nums[-1] = nums[i]
                    else:
                        final_nums.append(nums[i])
        return len(final_nums)

    def wiggleMaxLength_sol2(self, nums) -> int:
        positive_till_now = 1
        negative_till_now = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                positive_till_now = negative_till_now + 1
            elif nums[i] < nums[i - 1]:
                negative_till_now = positive_till_now + 1
        return max(positive_till_now, negative_till_now)


in_nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
a = Solution()
print(a.wiggleMaxLength(in_nums))
print(a.wiggleMaxLength_sol2(in_nums))


"""

Approach 1:
Check if the second number should be added then if the next number is greater than last number added, if the last 
difference was negative then add the next number else pass else if the number is smaller or equal then check if the new 
number is equal to last number then pass else if it the last difference is negative then replace the last number to the 
new one else just append

Approach 2:
Just keep track of number that is the difference between last added numbers was negative and positive, if the next 
difference is positive then add the negative till now + 1 to positive now one else add the positive till now + 1 to 
negative till now

Reference - https://leetcode.com/problems/wiggle-subsequence/discuss/1585932/100-efficient-Simple-Code-(Python3)%3A-O(n)

Complexities:
Time -> O(N)
Space -> O(N)

"""
