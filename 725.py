"""

---> Split Linked List in Parts
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
    def splitListToParts(self, head, k):
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length + 1

        chunk_size, longer_chunks = length // k, length % k
        ans = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)

        prev, curr = None, head
        print(ans)
        for index, num in enumerate(ans):
            if prev:
                prev.next = None
            ans[index] = curr
            for i in range(num):
                prev = curr
                curr = curr.next
        return ans


in_head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
in_k = 3
in_ll = to_linked_list(in_head)
a = Solution()
final = a.splitListToParts(in_ll, in_k)
for j in final:
    final_ans = "start -> "
    while j:
        final_ans += f"{j.val} -> "
        j = j.next
    final_ans += "end"
    print(final_ans)

"""

Find len of the linked list, find no. of nodes that each part should have then add that many to that part
Reference - https://leetcode.com/problems/split-linked-list-in-parts/discuss/109284/Elegant-Python-with-Explanation

Complexities:
Time -> O(N)
Space -> O(N)

"""
