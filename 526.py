"""

---> Beautiful Arrangement
---> Medium

"""


class Solution:
    def countArrangement(self, n: int) -> int:
        def check(num1, num2):
            return num1 % num2 == 0 or num2 % num1 == 0

        ans = 0
        stack = [(0, 0)]

        while stack:
            path_len, bin_vis = stack.pop()
            if path_len == n:
                ans += 1
            for i in range(1, n + 1):
                curr_num = 1 << (i - 1)
                # print(i, visited, bin(bin_vis), bin(curr_num), i not in visited, not (curr_num & bin_vis))
                if not (curr_num & bin_vis) and check(i, path_len + 1):
                    stack.append((path_len + 1, bin_vis | curr_num))
        return ans


in_n = 3
a = Solution()
print(a.countArrangement(in_n))


"""

Use a stack to keep track if all the numbers in the array have been used
bin_vis keeps track of numbers visited
check func checks if the number satisfies the condition

"""
