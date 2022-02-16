"""

---> Serialize and Deserialize BST
---> Medium

"""
import math
from tree_func import *


class Codec:
    def serialize(self, root) -> str:
        def pre_order(node):
            if node:
                nonlocal ans
                ans += " " + str(node.value)
                pre_order(node.left)
                pre_order(node.right)

        ans = ""
        pre_order(root)
        return ans

    def deserialize(self, data: str):
        def decode(min_val, max_val):
            if values and min_val < values[0] < max_val:
                val = values.popleft()
                node = Node(val)
                node.left = decode(min_val, val)
                node.right = decode(val, max_val)
                return node

        values = deque(int(val) for val in data.split())
        return decode(-1 * math.inf, math.inf)


in_array = [1, 2, 3, 4, 5, 6]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Codec()
serialized = a.serialize(in_root)
print("Serialized - ", serialized, "\n")
pretty_print(a.deserialize(serialized))


"""

For serialize put the tree in pre-order or post-order and append in a string
For deserialize just traverse the string in whichever order it has been serialized in
Reference- https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93171/Python-O(-N-)-solution.-easy-to-understand

"""
