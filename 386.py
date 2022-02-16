"""

---> Lexicographical Numbers
---> Medium

"""


class Solution:
    def lexicalOrder(self, n: int):
        final_array = []
        num = 1
        while len(final_array) < n:
            if num <= n:
                final_array.append(num)
                num *= 10
            else:
                num = num // 10 + 1
                while num % 10 == 0:
                    num //= 10
        return final_array

    def lexicalOrder_sol2(self, n: int):
        def dfs(num):
            if num > n:
                return

            ans.append(num)

            for digit in range(0, 10):
                dfs(num * 10 + digit)

        ans = []
        for i in range(1, 10):
            dfs(i)

        return ans


in_n = 130
a = Solution()
print(a.lexicalOrder(in_n))
print(a.lexicalOrder_sol2(in_n))


"""

Approach 1:
For each number starting from 1 in order check if their are any numbers in multiples of 10 that are smaller than n, if 
their are then take them else come back to divide by 10

Approach 2:
Do a dfs go into 10 till you can and loop from adding 1 to 9 for every node till the number smaller than n

Reference - https://leetcode.com/problems/lexicographical-numbers/discuss/1658983/Python-iterative-O(n)-time-O(1)-space
"""
