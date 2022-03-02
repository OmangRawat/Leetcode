"""

---> Intersection of Two Linked Lists
---> Easy

"""
from linked_list_func import *


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        p1 = headA
        p2 = headB

        len_list1 = 0
        len_list2 = 0
        while p1 is not None:
            len_list1 += 1
            p1 = p1.next

        while p2 is not None:
            len_list2 += 1
            p2 = p2.next

        p1 = headA
        p2 = headB

        if len_list1 > len_list2:
            diff = len_list1 - len_list2
            for i in range(diff):
                p1 = p1.next
        else:
            diff = len_list2 - len_list1
            for i in range(diff):
                p2 = p2.next

        while p1.val != p2.val:
            print(p1.val, p2.val)
            p1 = p1.next
            p2 = p2.next

        return p1


in_arr1 = [4, 1, 8, 4, 5]
in_arr2 = [5, 6, 1, 8, 4, 5]
in_list1 = to_linked_list(in_arr1)
in_list2 = to_linked_list(in_arr2)
a = Solution()
print("Intersected at", a.getIntersectionNode(in_list1, in_list2).val)
