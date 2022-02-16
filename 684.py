"""

---> Redundant Connection
---> Medium

"""


class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        root = {i: i for i in range(1, n + 1)}

        def find_parent(comp):
            if root[comp] == comp:
                return comp
            return find_parent(root[comp])

        for i, j in edges:
            u = find_parent(i)
            v = find_parent(j)
            if u == v:
                return [i, j]
            else:
                root[v] = u


in_edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
a = Solution()
print(a.findRedundantConnection(in_edges))


"""

Make components whichever are connected using Union find then return if any of the component have same parent that means 
it has been already connected by any other edges

"""
