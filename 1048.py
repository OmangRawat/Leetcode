"""

---> Longest String Chain
---> Medium

"""


class Solution:
    def longest_str_chain(self, words) -> int:
        word_dict = {}
        for w in sorted(words, key=len):
            word_dict[w] = max(word_dict.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
            print(w, word_dict)
        return max(word_dict.values())


in_words = ["a", "b", "ba", "bca", "bda", "bdca"]
a = Solution()
print(a.longest_str_chain(in_words))


"""

Sort acc to length of the words
Run through all words and check if one less letter word is there in dict
Reference - https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution

Complexities:
Time -> max(O(NlogN), O(NS))
Space -> O(NS)

"""
