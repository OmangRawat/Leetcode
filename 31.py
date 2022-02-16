"""

---> Next Permutation
---> Medium

"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = len(nums) - 1

        while index > 0:
            if nums[index] > nums[index - 1]:
                break
            index -= 1

        if index == 0:
            nums.reverse()
            return
        else:
            next = index
            while next < len(nums) and nums[next] > nums[index - 1]:
                next += 1
            nums[index - 1], nums[next - 1] = nums[next - 1], nums[index - 1]
            nums[index:] = nums[index:][::-1]


in_nums = [3, 2, 1]
a = Solution()
print(a.nextPermutation(in_nums))
