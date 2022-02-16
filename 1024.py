"""

---> Video Stitching
---> Medium

"""
import cmath


class Solution:
    def videoStitching(self, clips, time: int) -> int:
        dp = [cmath.inf] * (time + 1)
        dp[0] = 0
        for i in range(1, time + 1):
            for start, end in clips:
                if start <= i <= end:
                    dp[i] = min(dp[start] + 1, dp[i])
        if dp[time] == cmath.inf:
            return -1
        return dp[time]

    def videoStitching_sol2(self, clips, time: int) -> int:



in_clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
in_time = 10
a = Solution()
print(a.videoStitching(in_clips, in_time))


"""
"""
