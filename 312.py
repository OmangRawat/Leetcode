"""

---> Burst Balloons
---> Hard

"""


# Python3 program burst balloon problem.

def getMax(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for x in range(n + 2)] for y in range(n + 2)]

    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for last in range(left, right + 1):
                dp[left][right] = max(dp[left][right], dp[left][last - 1] + nums[left - 1] * nums[last] * nums[right + 1] +
                                      dp[last + 1][right])
    return dp[1][n]


# Driver code
A = [9, 76, 64, 21, 97, 60]
print(getMax(A))
