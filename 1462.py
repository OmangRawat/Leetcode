"""

---> Course Schedule IV
---> Medium

"""
from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        course_used = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque([])
        courses_needed = defaultdict(set)

        for c1, c2 in prerequisites:
            course_used[c1].append(c2)
            in_degree[c2] += 1

        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)
                courses_needed[node] = set()

        while queue:
            node = queue.popleft()

            for course in course_used[node]:
                in_degree[course] -= 1
                courses_needed[course].update(courses_needed[node])
                courses_needed[course].add(node)
                if in_degree[course] == 0:
                    queue.append(course)

        return [c1 in courses_needed[c2] for c1, c2 in queries]


in_courses = 3
in_pre = [[1, 2], [1, 0], [2, 0]]
in_queries = [[1, 0], [1, 2]]
a = Solution()
print(a.checkIfPrerequisite(in_courses, in_pre, in_queries))


"""
Reference - https://leetcode.com/problems/course-schedule-iv/discuss/1642474/Python-BFS-with-set
"""
