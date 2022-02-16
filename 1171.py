"""

---> Remove Zero Sum Consecutive Nodes from Linked List
---> Medium

"""
from linked_list_func import *


class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0, head)
        pre = 0
        dic = {0: dummy_head}

        while head:
            pre += head.val
            dic[pre] = head
            head = head.next

        head = dummy
        pre = 0
        while head:
            pre += head.val
            head.next = dic[pre].next
            head = head.next

        return dummy.next



