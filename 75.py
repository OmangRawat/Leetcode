"""

---> Sort Colors
---> Medium

"""
from collections import Counter


class Solution:
    def sortColors(self, nums) -> None:
        freq = Counter(nums)
        index = 0
        for color in range(3):
            for _ in range(freq[color]):
                nums[index] = color
                index += 1


in_nums = [2, 0, 2, 1, 1, 0]
a = Solution()
a.sortColors(in_nums)
print(in_nums)
