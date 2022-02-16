"""

---> Maximum Subarray Sum with One Deletion
---> Medium

"""
import math
array = [-1, -1, -1, -1]


class Solution:
    def maximum_sum(self, arr) -> int:
        without_0, without_1, res = 0, 0, max(arr)
        for i in arr:
            if i >= 0:
                without_0 += i
                without_1 += i
            else:
                without_1 = max(without_1 + i, without_0)
                without_0 += i

            # res = max(res, without_0, without_1)
            res = max([res, without_1 if without_1 != 0 else -math.inf, without_0])
            if without_0 < 0:
                without_0 = 0
            if without_1 < 0:
                without_1 = 0
        # return max(res, max(arr))
        return res


a = Solution()
print(a.maximum_sum(array))

"""

As it is only 1 can be deleted without_1 = either ignoring the current value or 1 value has already been ignored
res value is working because the ans can be 0 only if all the no. in array are negative and just 1 is 0 so max at last 
will take care of it


Complexities:
Time ->  O(N)
Space -> O(1)

"""


