"""

---> Letter Case Permutation
---> Medium

"""


class Solution:
    def letterCasePermutation(self, s: str):
        def permute(char_index):
            if char_index > max_len:
                ans.append(''.join(s_list))
                return
            permute(char_index + 1)
            if s_list[char_index].isalpha():
                s_list[char_index] = s_list[char_index].swapcase()
                permute(char_index + 1)
                s_list[char_index] = s_list[char_index].swapcase()

        ans = []
        max_len = len(s) - 1
        s_list = list(s)
        permute(0)
        return ans


in_s = "a1b2"
a = Solution()
print(a.letterCasePermutation(in_s))


"""

Use swapcase() func to swap cases whenever there is an alphabet found until all the letter have been done and then add 
it to the ans array then change it back

"""
