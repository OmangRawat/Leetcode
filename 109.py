"""

---> Convert Sorted List to Binary Search Tree
---> Medium

"""
from tree_func import *
from linked_list_func import to_linked_list


class Solution:
    def sortedListToBST(self, head):
        def length(in_head):
            ll_len = 0
            while in_head:
                ll_len += 1
                in_head = in_head.next
            return ll_len

        def dfs(left, right):
            nonlocal head
            if left > right:
                return None
            mid = (left + right) // 2
            left_node = dfs(left, mid - 1)

            root = Node(head.val)
            head = head.next

            root.left = left_node
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, length(head) - 1)


in_list = [-10, -3, 0, 5, 9]
in_ll = to_linked_list(in_list)
ans = "start -> "
while in_ll:
    ans += f"{in_ll.val} -> "
    in_ll = in_ll.next
ans += "end"
print(ans)
a = Solution()
pretty_print(a.sortedListToBST(in_ll))


"""

Reference - https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/596899/JavaPython-2-solutions-Clean-and-Concise-O(N)-time-O(logN)-space

Approach 1:
Store all elements in array and find mid ele and divide array accordingly into left and right sub tree

Approach 2:
Find len of list find mid ele divide elements before that into left sub tree make the curr element root and elements 
after to right 

"""
