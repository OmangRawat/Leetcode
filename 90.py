"""

---> Subsets II
---> Medium

"""


class Solution:
    def subsetsWithDup(self, nums):
        lists = [[]]
        nums.sort()

        for i in nums:
            for j in range(len(lists)):
                lists.append(lists[j] + [i])

        ans = []
        for i in lists:
            if i not in ans:
                ans.append(i)

        return ans


in_nums = [1, 2, 2]
a = Solution()
print(a.subsetsWithDup(in_nums))
