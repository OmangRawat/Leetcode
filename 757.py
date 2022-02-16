"""

---> Set Intersection Size At Least Two
---> Hard

"""


class Solution:
    def intersectionSizeTwo(self, intervals) -> int:
        ans, end1, end2 = 0, -1, -1
        final = set()
        for start, end in sorted(intervals, key=lambda x: (x[1], -x[0])):
            if start <= end1:
                pass
            if end1 < start <= end2:
                ans += 1
                end1, end2 = end2, end
                final.add(end1)
                final.add(end2)
            if start > end2:
                ans += 2
                end1, end2 = end - 1, end
                final.add(end1)
                final.add(end2)
            print(final)

        return ans


in_intervals = [[1, 3], [3, 7], [4, 7]]
a = Solution()
print(a.intersectionSizeTwo(in_intervals))


"""

Keep track of last 2 numbers in the final set, sort the array ascending according to end of the set and descending of 
the ones having same end that will make every next set end coming to be greater than all the number already added in the 
final set thus we just need to check position of start
If the start comes before the 2 numbers then we already have common numbers
If the start is between las t 2 numbers then their is already 1 common number we need to add 1 more that would be the 
largest one we can add
If the start is after all the numbers in the set then we need to add 2 numbers more that would be best end -1 and end

Reference - https://leetcode.com/problems/set-intersection-size-at-least-two/discuss/986968/Python3-Greedy-O(NlogN)

"""
