"""

---> Product of Array Except Self
---> Medium

"""


class Solution:
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)

        product_from_left = 1
        for i in range(0, len(nums)):
            ans[i] = product_from_left
            product_from_left *= nums[i]

        product_from_right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= product_from_right
            product_from_right *= nums[i]
        return ans


in_nums = [-1, 1, 0, -3, 3]
a = Solution()
print(a.productExceptSelf(in_nums))


"""

Get an array of product till 1 element left of the number
Get an array of product till 1 element right of the number
Multiply them for every "i"

"""
