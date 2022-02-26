"""

---> Remove Nth Node From End of List
---> Medium

"""
from linked_list_func import *


class Solution:
    def removeNthFromEnd(self, head, n: int):
        slow = head
        fast = head

        for i in range(0, n):
            if fast.next is None:
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow.next is not None:
            slow.next = slow.next.next
        return head


in_arr = [1, 2, 3, 4, 5]
in_n = 2
in_head = to_linked_list(in_arr)
a = Solution()
print_list(a.removeNthFromEnd(in_head, in_n))
