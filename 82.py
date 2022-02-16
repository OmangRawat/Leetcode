"""

---> Remove Duplicates from Sorted List II
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
    def deleteDuplicates(self, head):
        ans_start = ListNode(-1)
        ans_start.next = head
        prev, curr = ans_start, ans_start.next

        while curr:
            if curr.next and curr.val == curr.next.val:
                val_to_rem = curr.val

                while curr and curr.val == val_to_rem:
                    curr = curr.next

                prev.next = curr

            else:
                prev, curr = curr, curr.next

        return ans_start.next


in_head = [1, 2, 3, 3, 4, 4, 5]
in_ll = to_linked_list(in_head)
a = Solution()
ans_ll = a.deleteDuplicates(in_ll)
ans = "start -> "
while ans_ll:
    ans += f"{ans_ll.val} -> "
    ans_ll = ans_ll.next
ans += "end"
print(ans)


"""

As list is sorted check if the next element is same, if it is then skip nodes equal to that value of the node
Reference - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28398/clean-python-solution-involving-dummy-node

Complexities:
Time -> 
Space -> 

"""
