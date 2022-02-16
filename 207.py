"""

---> Course Schedule
---> Medium

"""
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        # DFS
        course_graph, in_degree, ans = defaultdict(list), [0] * numCourses, 0

        for c1, c2 in prerequisites:
            course_graph[c2].append(c1)
            in_degree[c1] += 1

        def dfs(cur_course):
            nonlocal ans
            ans += 1
            in_degree[cur_course] = -1

            for nextCourse in course_graph[cur_course]:
                in_degree[nextCourse] -= 1
                if in_degree[nextCourse] == 0:
                    dfs(nextCourse)

        for c in range(numCourses):
            if in_degree[c] == 0:
                dfs(c)

        return True if ans == numCourses else False

    def canFinish_sol2(self, numCourses, prerequisites) -> bool:
        # Check for cycles
        def is_cycle(course):
            cycle_record[course] = 1
            visited[course] = 1

            if course in course_graph:
                for j in course_graph[course]:
                    if visited[j] == 0:
                        if is_cycle(j):
                            return True
                    elif cycle_record[j] == 1:
                        return True

            cycle_record[course] = 0
            return False

        n = len(prerequisites)
        course_graph = defaultdict(list)

        for i in range(n):
            course_graph[prerequisites[i][0]].append(prerequisites[i][1])

        cycle_record = [0 for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]

        for i in course_graph:
            if visited[i] == 0 and is_cycle(i):
                return False

        return True


in_courses = 2
in_pre = [[1, 0]]
a = Solution()
print(a.canFinish(in_courses, in_pre))


"""

Approach 1:

Approach 2:
Reference - https://leetcode.com/problems/course-schedule/discuss/1598607/Python-or-Easy-to-understand-or-Check-if-there-is-a-Cycle-using-DFS

Approach 3:
Kahn's Algo

"""
