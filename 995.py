"""

---> Minimum Number of K Consecutive Bit Flips
---> Hard

"""


class Solution:
    def minKBitFlips(self, nums, k: int) -> int:
        flipped, ans, n = 0, 0, len(nums)
        flip = [False] * len(nums)

        for i in range(n):
            if i >= k and flip[i - k]:
                flipped = not flipped
                flip[i - k] = False
            if flipped % 2 == nums[i]:
                if i + k > n:
                    return -1
                flipped = not flipped
                flip[i] = True
                ans += 1

        return ans


in_nums = [1, 1, 0]
# in_nums = [0, 0, 0, 1, 0, 1, 1, 0]
in_k = 2
a = Solution()
print(a.minKBitFlips(in_nums, in_k))


"""

-> flipped represents if last bit has been flipped or not
-> flip represents if for every index the bit was flipped or not
-> for i >= k you need to check for the flipped and if the bit was flipped for i - k as that would tell if the last bit 
was flipped even or odd no. of times till i - 1 bit 
-> For eg. if the bit i - k bit was flipped odd no. of times and again odd no.  of times inside the window then total 
would be even for i- 1th bit but the ones affecting the ith bit are the ones that are only inside the window thus we 
would take it as odd flips till i - 1 th to check for if the ith bit needs to be flipped

"""
