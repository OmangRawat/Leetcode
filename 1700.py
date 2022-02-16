"""

---> Number of Students Unable to Eat Lunch
---> Easy

"""
import collections


class Solution:
    def countStudents(self, students, sandwiches) -> int:
        while sandwiches:
            if sandwiches[0] in students:
                students.remove(sandwiches[0])
                sandwiches.pop(0)
            else:
                break
        return len(sandwiches)

    def countStudents_sol2(self, students, sandwiches) -> int:
        count = collections.Counter(students)
        n, k = len(students), 0
        while k < n and count[sandwiches[k]]:
            count[sandwiches[k]] -= 1
            k += 1
        return n - k


in_students = [1, 1, 1, 0, 0, 1]
in_sandwiches = [1, 0, 0, 0, 1, 1]
a = Solution()
# print(a.countStudents(in_students, in_sandwiches))
print(a.countStudents_sol2(in_students, in_sandwiches))

"""

Approach 1:
If the first element of sandwich is needed by a student then pop and continue else break
Reference - https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/discuss/997823/100-speed-Python-No-importsSimple-to-understand-commented!

Complexities:
Time -> O(N^2)
Space -> O(1)


Approach 2:
Count the number of students that ant each type of sandwiches
Reference - https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/discuss/987403/JavaC%2B%2BPython-Easy-and-Concise

Complexities:
Time -> O(N)
Space -> O(1)

"""
