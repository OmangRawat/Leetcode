"""

---> Merge Two Sorted Lists
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
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


in_list_1 = [1, 2, 4]
in_list2 = [1, 3, 4]
in_ll1 = to_linked_list(in_list_1)
in_ll2 = to_linked_list(in_list2)
a = Solution()
merged_ll = a.mergeTwoLists(in_ll1, in_ll2)
ans = "start -> "
while merged_ll:
    ans += f"{merged_ll.val} -> "
    merged_ll = merged_ll.next
ans += "end"
print(ans)


"""
Take one element from each, compare and continue
Reference - https://leetcode.com/problems/merge-two-sorted-lists/discuss/759870/Python3-Solution-with-a-Detailed-Explanation-dummy-explained
"""
