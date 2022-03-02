"""

---> Linked List Cycle
---> Easy

"""
from linked_list_func import *


class Solution:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


in_head = [3, 2, 0, -4]
in_pos = 1
in_list = to_linked_list(in_head)
p = in_list
while p.next:
    p = p.next
q = in_list
while in_pos:
    q = q.next
    in_pos -= 1
p.next = q
a = Solution()
print(a.hasCycle(in_list))
