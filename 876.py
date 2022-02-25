"""

---> Middle of the Linked List
---> Easy

"""
from linked_list_func import *


class Solution:
    def middleNode(self, head):
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        if length % 2 == 0:
            mid = int(length / 2) + 1
            while mid > 1:
                head = head.next
                mid -= 1

            return head
        else:
            mid = int((length + 1) / 2)
            while mid > 1:
                head = head.next
                mid -= 1

            return head


in_arr = [1, 2, 3, 4, 5, 6]
in_head = to_linked_list(in_arr)
a = Solution()
print_list(a.middleNode(in_head))
