"""

---> Reverse Linked List
---> Easy

"""
from linked_list_func import *


class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


in_arr = [1, 2, 3, 4, 5]
in_list = to_linked_list(in_arr)
print_list(in_list)
a = Solution()
print_list(a.reverseList(in_list))
