"""

---> Boats to Save People
---> Medium

"""


class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        n = len(people)
        left, right = 0, n - 1
        boat = 0
        while True:

            if people[left] + people[right] <= limit:
                left += 1

            boat += 1

            if left >= right:
                break

            right -= 1

        return boat


in_people = [3, 5, 3, 4]
in_limit = 5
a = Solution()
print(a.numRescueBoats(in_people, in_limit))


"""
Take 2 pointers from the smallest and greatest weight, decrease the greatest ele with every turn and increase the left 
pointer whenever the sum of the pair is less than equal to limit
Reference - https://leetcode.com/problems/boats-to-save-people/discuss/1014526/Python-O(n-lg-n)-by-two-pointers-and-sort-w-Comment
"""
