"""

---> Delete Node in a Linked List
---> Easy

"""
from linked_list_func import *


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
        
in_head = [4, 5, 1, 9]
in_list = to_linked_list(in_head)
in_node = in_list.next
a = Solution()
a.deleteNode(in_node)
print_list(in_list)
