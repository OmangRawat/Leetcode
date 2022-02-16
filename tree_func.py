from collections import deque, defaultdict
from ppbtree import *


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def to_binary_tree(a, root=None):
#     Q = deque()
#
#     def insert_node(data, next_root):
#         print(data, type(data))
#         new_node = Node(data)
#         if Q:
#             temp = Q[0]
#
#         if not next_root:
#             next_root = new_node
#
#         elif not temp.left:
#             if not data:
#                 temp.left = new_node
#             else:
#                 temp.left = None
#
#         elif not temp.right:
#             if not data:
#                 temp.right = new_node
#             else:
#                 temp.right = None
#             Q.popleft()
#
#         if not data:
#             Q.append(new_node)
#         return next_root
#
#     for i in range(len(a)):
#         root = insert_node(a[i], root)
#         pretty_print(root)
#     return root


def to_binary_tree(a, root=None):
    Q = deque()

    def insert_node(data, next_root):
        new_node = Node(data)

        if not next_root:
            next_root = new_node

        if Q:
            temp = Q[0][0]
            if not Q[0][1]:
                if data:
                    temp.left = new_node
                Q[0][1] = True

            elif not Q[0][2]:
                if data:
                    temp.right = new_node
                Q.popleft()

        if data:
            Q.append([new_node, False, False])
            # stores the pointer to node, if left has been appended on and right has been appended on or not
        return next_root

    for i in range(len(a)):
        root = insert_node(a[i], root)
        # pretty_print(root)
    return root


def pretty_print(in_tree):
    print("'Tree is kind of reversed, Take up as left and down as right'\n")
    print_tree(in_tree)
    print("\n")
