"""

---> Permutation Sequence
---> Hard

"""
from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def get_perm(arr_left, k_left):
            print("k_left", k_left)
            nonlocal ans
            if len(arr_left) == 1 or k_left == 0:
                print("arr_left", arr_left)
                ans += "".join(str(x) for x in arr_left)
            else:
                a = k_left // factorial(len(arr_left) - 1)
                k_left %= factorial(len(arr_left) - 1)
                print("a", a)
                ans += str(arr_left[a])
                arr_left = arr_left[:a] + arr_left[a + 1:]
                print(ans)
                get_perm(arr_left, k_left)
        ans = ""
        arr = [x for x in range(1, n + 1)]
        get_perm(arr, k - 1)
        return ans


in_n = 2
in_k = 2
a = Solution()
print(a.getPermutation(in_n, in_k))
