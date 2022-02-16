"""

---> Merge Intervals
---> Medium

"""


class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans = [intervals[0]]
        for interval in intervals[1:]:
            if ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


in_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
a = Solution()
print(a.merge(in_intervals))
