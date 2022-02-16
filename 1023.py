"""

---> Camelcase Matching
---> Medium

"""
from collections import defaultdict
from trie_func import trie_print


class Solution:
    def camelMatch(self, queries, pattern: str):
        # def trie():
        #     return defaultdict(trie)

        def check(word):
            # trie_print(word_dict)
            # current = word_dict
            p_index = 0
            follow_pattern = True
            for letter in word:
                if p_index < len(pattern) and letter == pattern[p_index]:
                    p_index += 1
                elif p_index < len(pattern) and letter.isupper() and letter != pattern[p_index]:
                    follow_pattern = False
                    break
                elif p_index == len(pattern) and letter.isupper():
                    follow_pattern = False
                    break
            #     current = current[letter]
            # current['word'] = word

            return follow_pattern and p_index == len(pattern)

        # word_dict = trie()
        return [check(word) for word in queries]


in_queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
in_pattern = "FoBaT"
a = Solution()
print(a.camelMatch(in_queries, in_pattern))


"""

Run a loop for the pattern if you find the element in the word check for next element in the pattern 
If you fnd a different upper case instead of needed one then return false
If after the pattern has been finished checking check if their are anymore upper case letters left in the respective 
word

"""
