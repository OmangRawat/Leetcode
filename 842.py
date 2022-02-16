"""

---> Split Array into Fibonacci Sequence
---> Medium

"""


class Solution:
    def splitIntoFibonacci(self, num: str):
        def dfs(i):
            if i >= len(num):
                return len(ans) > 2
            n = 0
            for j in range(i, len(num)):
                n = n * 10 + int(num[j])

                if n >= 2 ** 31:
                    return False

                if len(ans) < 2 or (ans[-1] + ans[-2] == n):
                    ans.append(n)
                    if dfs(j + 1):
                        return True
                    ans.pop()

                if i == j and num[j] == '0':
                    return False

        if len(num) > 2:
            ans = []
            if dfs(0):
                return ans

        return []


in_nums = "1101111"
a = Solution()
print(a.splitIntoFibonacci(in_nums))


"""
"""
