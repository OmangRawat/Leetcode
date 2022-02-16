"""

---> Maximum XOR of Two Numbers in an Array
---> Medium

"""


class Solution:
    def findMaximumXOR(self, nums) -> int:
        def fill_trie(x):
            cur = trie
            for bit in format(x, '032b'):
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]
            cur['val'] = x

            return

        def best_match(x):
            cur = trie

            for bit in format(x, '032b'):
                rev = '0' if bit == '1' else '1'
                if rev in cur:
                    cur = cur[rev]
                else:
                    cur = cur[bit]

            return cur['val']

        trie = {}

        for num in nums:
            fill_trie(num)
        print(trie)
        ans = 0
        for num in nums:
            ans = max(ans, num ^ best_match(num))

        return ans


in_nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
a = Solution()
print(a.findMaximumXOR(in_nums))


"""
Best XOR of two numbers is when you have a pair of a number and closest number to its complement
So fill a trie with all the numbers then try to find the nearest number to the complement of that number in the trie
"""
