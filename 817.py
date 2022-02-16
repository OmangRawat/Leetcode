"""

---> Linked List Components
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
    def numComponents(self, head, nums) -> int:
        num_set = set(nums)
        ans = 0
        while head:
            if (head.val in num_set) and (head.next is None or head.next.val not in num_set):
                ans += 1
            head = head.next
        return ans


in_head = [0, 1, 2, 3, 4]
in_nums = [0, 3, 1, 4]
in_ll = to_linked_list(in_head)
a = Solution()
print(a.numComponents(in_ll, in_nums))


"""

Keep track of last nodes in linked list, whenever the next element is not in the nums set or is none end the component
Reference - https://leetcode.com/problems/linked-list-components/discuss/933679/Python3-counting-end-of-component

Complexities:
Time -> O(N)
Space -> O(M)

"""
