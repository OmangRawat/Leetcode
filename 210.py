"""

---> Course Schedule II
---> Medium

"""
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        # BFS
        course_graph, in_degree, queue, ans = defaultdict(list), [0] * numCourses, deque(), []

        for c1, c2 in prerequisites:
            course_graph[c2].append(c1)
            in_degree[c1] += 1

        for c in range(numCourses):
            if in_degree[c] == 0:
                queue.append(c)

        while queue:
            cur_course = queue.popleft()
            ans.append(cur_course)

            for nextCourse in course_graph[cur_course]:
                in_degree[nextCourse] -= 1
                if in_degree[nextCourse] == 0:
                    queue.append(nextCourse)

        return ans if len(ans) == numCourses else []

    def findOrder_sol2(self, numCourses, prerequisites):
        # DFS
        course_graph, in_degree, ans = defaultdict(list), [0] * numCourses, []

        for c1, c2 in prerequisites:
            course_graph[c2].append(c1)
            in_degree[c1] += 1

        def dfs(cur_course):
            ans.append(cur_course)
            in_degree[cur_course] = -1

            for nextCourse in course_graph[cur_course]:
                in_degree[nextCourse] -= 1
                if in_degree[nextCourse] == 0:
                    dfs(nextCourse)

        for c in range(numCourses):
            if in_degree[c] == 0:
                dfs(c)

        return ans if len(ans) == numCourses else []


in_courses = 2
in_pre = [[1, 0]]
a = Solution()
print(a.findOrder(in_courses, in_pre))
print(a.findOrder_sol2(in_courses, in_pre))


"""
Reference - https://leetcode.com/problems/course-schedule-ii/discuss/1642354/C%2B%2BPython-Simple-Solutions-w-Explanation-or-Topological-Sort-using-BFS-and-DFS
"""
