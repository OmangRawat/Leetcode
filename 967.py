"""

---> Numbers With Same Consecutive Differences
---> Medium

"""


class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        def get_number(num):
            if len(num) == n:
                ans.append(''.join([str(x) for x in num]))
                return

            last_digit = num[-1]
            for next_digit in {last_digit - k, last_digit + k}:
                if 0 <= next_digit <= 9:
                    num.append(next_digit)
                    get_number(num)
                    num.pop()

        ans = []
        for i in range(1, 10):
            get_number([i])

        return ans


in_n = 3
in_k = 3
a = Solution()
print(a.numsSameConsecDiff(in_n, in_k))


"""

Start from 1 as the first digit and move forward check for every previous digit if you can find next digit with a 
difference of k from it add it to the number and so on
When you find the length of the number as equal to n then join all digits in the array to get the required number

Reference - https://leetcode.com/problems/numbers-with-same-consecutive-differences/discuss/993038/Clean-Python-or-DFS-and-BFS

"""
