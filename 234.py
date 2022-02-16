"""

---> Palindrome Linked List
---> Easy

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next

        return True


in_head = [1, 2]
a = Solution()

for i in range(len(in_head)):
    if i == 0:
        ln = ListNode(i)
        head = ln
    elif i == len(in_head) - 1:
        ln.next = ListNode(in_head[i])
        ln = ln.next
        ln.next = None
    else:
        ln.next = ListNode(in_head[i])
        ln = ln.next


print(a.isPalindrome(head))


"""

Find the mid then reverse the string till their and compare with after half string

Complexities:
Time -> O(N)
Space -> O(N)

"""
