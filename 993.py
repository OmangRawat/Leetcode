"""

---> Cousins in Binary Tree
---> Easy

"""
from collections import deque, defaultdict
from ppbtree import *


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def to_binary_tree(a, root=None):
    Q = deque()

    def insert_node(data, next_root):
        new_node = Node(data)
        temp = None
        if Q:
            temp = Q[0]

        if not next_root:
            next_root = new_node

        elif not temp.left:
            temp.left = new_node

        elif not temp.right:
            temp.right = new_node
            Q.popleft()

        Q.append(new_node)
        return next_root

    for i in range(len(a)):
        root = insert_node(a[i], root)
    return root


def pretty_print(in_tree):
    print("'Tree is kind of reversed, Take up as left and down as right'\n")
    print_tree(in_tree)
    print("\n")


class Solution:
    def isCousins(self, root, x, y):
        # DFS
        def dfs(node, parent, depth: int):
            if not node or len(ans_nodes) == 2:
                return
            else:
                if node.value == x or node.value == y:
                    ans_nodes.append((parent, depth))
                dfs(node.left, node, depth + 1)
                dfs(node.right, node, depth + 1)

        ans_nodes = []
        dfs(root, None, 0)
        print(ans_nodes)
        pretty_print(ans_nodes[0][0])
        pretty_print(ans_nodes[1][0])

        return ans_nodes[0][0] != ans_nodes[1][0] and ans_nodes[0][1] == ans_nodes[1][1]

    def isCousins_sol2(self, root, x, y):
        # BFS
        nodes_list = defaultdict(list)
        queue = [(root, 0, 0)]
        while queue:
            node, depth, parent = queue.pop(0)
            nodes_list[node.value] = [depth, parent]

            if node.left:
                queue.append((node.left, depth + 1, node.value))
            if node.right:
                queue.append((node.right, depth + 1, node.value))

        if nodes_list[x][0] == nodes_list[y][0] and nodes_list[x][1] != nodes_list[y][1]:
            return True

        return False


in_array = [1, 2, 3, None, 4, None, 5]
in_x = 5
in_y = 4
in_root = to_binary_tree(in_array)
a = Solution()
print(a.isCousins(in_root, in_x, in_y))
print(a.isCousins_sol2(in_root, in_x, in_y))


"""

Keep track of parent and depth
DFS
Reference - https://leetcode.com/problems/cousins-in-binary-tree/discuss/246883/Python-straightforward-and-clean-DFS

BFS
Reference - https://leetcode.com/problems/cousins-in-binary-tree/discuss/299889/Python-BFS-solution

"""
