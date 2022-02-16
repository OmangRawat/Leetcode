"""

---> Partition List
---> Medium

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(in_list):
    head = ln = ListNode()
    for i in range(len(in_list)):
        if i == 0:
            ln = ListNode(in_list[i])
            head = ln
        elif i == len(in_list) - 1:
            ln.next = ListNode(in_list[i])
            ln = ln.next
            ln.next = None
        else:
            ln.next = ListNode(in_list[i])
            ln = ln.next
    return head


class Solution:
    def partition(self, head, x: int):
        start1 = ListNode(-1)
        start2 = ListNode(-1)
        pointer1, pointer2 = start1, start2

        while head:
            if head.val < x:
                pointer1.next = head
                pointer1 = pointer1.next
            else:
                pointer2.next = head
                pointer2 = pointer2.next
            # print(head.val, pointer1.val, pointer2.val)
            head = head.next

        pointer1.next = start2.next
        pointer2.next = None

        return start1.next


in_head = [1, 4, 3, 2, 5, 2]
in_x = 3
in_ll = to_linked_list(in_head)
a = Solution()
merged_ll = a.partition(in_ll, in_x)
ans = "start -> "
while merged_ll:
    ans += f"{merged_ll.val} -> "
    merged_ll = merged_ll.next
ans += "end"
print(ans)


"""

Make 2 Linked List, one containing numbers smaller than x in same order and other having numbers greater than x
then join them
Reference - https://leetcode.com/problems/partition-list/discuss/1157788/Python-Two-Pointers-explained

Complexities:
Time -> O(N)
Space -> O(1)

"""
