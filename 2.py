"""

---> Add Two Numbers
---> Medium

"""
from linked_list_func import *


class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = str(l1.val)
        num2 = str(l2.val)

        while l1.next:
            num1 = str(l1.next.val) + num1
            l1 = l1.next

        while l2.next:
            num2 = str(l2.next.val) + num2
            l2 = l2.next

        n1 = int(num1)
        n2 = int(num2)

        total = n1 + n2
        total_str = str(total)

        head = ListNode(int(total_str[0]), None)
        for i in range(1, len(total_str)):
            sum_list = ListNode(int(total_str[i]), head)
            head = sum_list

        return head


in_arr1 = [2, 4, 3]
in_arr2 = [5, 6, 4]
in_l1 = to_linked_list(in_arr1)
in_l2 = to_linked_list(in_arr2)
a = Solution()
print_list(a.addTwoNumbers(in_l1, in_l2))
