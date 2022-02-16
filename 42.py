"""

---? Trapping Rain Water
---? Hard

"""


class Solution:
    def trap(self, height) -> int:
        total_water = 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i - 1])

        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(len(height)):
            total_water += (min(left_max[i], right_max[i]) - height[i])

        return total_water


in_height =
a = Solution()
print(a.trap(in_height))
