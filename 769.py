"""

---> Max Chunks To Make Sorted
---> Medium

"""


class Solution:
    def maxChunksToSorted(self, arr) -> int:
        stack = []
        for x in arr:
            cur = (x, x)
            while stack and stack[-1][1] > cur[0]:
                top = stack.pop()
                cur = (min(top + cur), max(top + cur))
            stack.append(cur)
            # print(stack)
        return len(stack)

    def maxChunksToSorted_sol2(self, arr) -> int:
        chunks = 0
        max_till_now = arr[0]
        for i in range(len(arr)):
            max_till_now = max(max_till_now, arr[i])
            if i == max_till_now:
                chunks += 1
        return chunks


in_arr = [1, 4, 0, 2, 3, 5]
a = Solution()
print(a.maxChunksToSorted(in_arr))
# print(a.maxChunksToSorted_sol2(in_arr))


"""
Approach 1:
Keep track of number of chunks we need to make with its minimum and maximum element, whenever an element greater than
the max of chunk comes combine it with the last chunk
Reference - https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/185481/Python-O(n)-with-stack

Complexities:
Time -> O(N^2)
Space -> O(N)


Approach 2:
As the numbers in the array are from 0 to n - 1, when the array is sorted it will have element equal to the index in
the array so when you find the max number in chunk equal to the index make the chunk end there as number ahead of it will always be greater than the max number
Reference - https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/138844/Python-O(n)-Very-Detailed-Explanation

Complexities:
Time -> O(N)
Space -> O(1)

"""
