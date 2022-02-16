"""

---> Odd Even Linked List
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
    def oddEvenList(self, head):
        start_odd = ListNode(-1)
        start_even = ListNode(-1)
        pointer_odd, pointer_even = start_odd, start_even

        while head:
            pointer_odd.next = head
            pointer_odd = pointer_odd.next

            pointer_even.next = head.next
            pointer_even = pointer_even.next

            if pointer_even:
                head = head.next.next
            else:
                head = None

        pointer_odd.next = start_even.next

        return start_odd.next


in_head = [2, 1, 3, 5, 6, 4, 7]
in_ll = to_linked_list(in_head)
a = Solution()
merged_ll = a.oddEvenList(in_ll)
ans = "start -> "
while merged_ll:
    ans += f"{merged_ll.val} -> "
    merged_ll = merged_ll.next
ans += "end"
print(ans)


"""
Make 2 linked list one having odd ones and other having even ones then join them 
"""
