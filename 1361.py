"""

---> Validate Binary Tree Nodes
---> Medium

"""
from collections import deque


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        # BFS
        def find_root():    # Should have one root
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1

        root = find_root()

        if root == -1:
            return False

        queue = deque([root])
        visited = set()

        while queue:

            cur = queue.popleft()

            if cur in visited:      # Should not have any cycles
                return False        # Each node should have one one parent

            visited.add(cur)

            if leftChild[cur] != -1:
                queue.append(leftChild[cur])

            if rightChild[cur] != -1:
                queue.append(rightChild[cur])

        return len(visited) == n   # Should visit all nodes without repeating any


in_n = 4
in_left = [1, -1, 3, -1]
in_right = [2, -1, -1, -1]
a = Solution()
print(a.validateBinaryTreeNodes(in_n, in_left, in_right))


"""
Reference - https://leetcode.com/problems/validate-binary-tree-nodes/discuss/1625191/Python-O(n)-by-DFS-BFS-UnionFind-w-Comment
"""
