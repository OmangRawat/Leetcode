"""

---> Convert Binary Number in a Linked List to Integer
---> Easy

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
    def getDecimalValue(self, head) -> int:
        ans = 0
        while head:
            ans = 2 * ans + head.val
            head = head.next
        return ans


in_head = [1, 0, 1]
in_ll = to_linked_list(in_head)
a = Solution()
print(a.getDecimalValue(in_ll))


"""

Whenever you go to next node double last ans and add whatever the node is 1 or 0 to it
Reference - https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/455239/Python-Simple.-20ms.

Complexities:
Time -> O(N)
Space -> O(1)

"""
