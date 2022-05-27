"""

---> Count Triplets That Can Form Two Arrays of Equal XOR
---> Medium

"""
from collections import defaultdict


class Solution:
    def countTriplets(self, arr) -> int:
        xor_sum = defaultdict(list)
        xor_sum[0].append(-1)
        curr_xor, ans = 0, 0
        for i in range(len(arr)):
            curr_xor ^= arr[i]
            if curr_xor in xor_sum:
                for j in xor_sum[curr_xor]:
                    print(curr_xor, i, j, i - j)
                    ans += (i - j - 1)
            xor_sum[curr_xor].append(i)
            print(xor_sum)
        return ans


in_arr = [2, 3, 5, 1, 2, 6, 2, 7]
a = Solution()
print(a.countTriplets(in_arr))


"""

Store indices for each xor_sum in a dictionary 
For every time the sum occurs again we can take the sub-array from j + 1 to i that will give us i - (j - 1) triplets 
Eg. 5 - 1 6 7 and 5 1 - 6 7 and 5 1 6 - 7 i.e. 5 - (1 + 1)

"""

