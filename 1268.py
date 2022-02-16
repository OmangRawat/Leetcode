"""

---> Search Suggestions System
---> Medium

"""
from collections import defaultdict
from functools import reduce


class Solution:
    def suggestedProducts(self, products, searchWord: str):
        def trie():
            return defaultdict(trie)

        def get_top3(start_dict):
            def helper(in_dict):
                if len(top3) >= 3:
                    return
                if 'end' in in_dict:
                    top3.append(in_dict['end'])

                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char in in_dict:
                        helper(in_dict[char])

            top3 = []
            helper(start_dict)
            return top3

        word_dict = trie()

        for product in products:
            reduce(dict.__getitem__, product, word_dict)['end'] = product

        ans = []
        curr_dict = word_dict
        for index, letter in enumerate(searchWord):
            if letter not in curr_dict:
                break
            curr_dict = curr_dict[letter]
            ans.append(get_top3(curr_dict))

        ans += [[] for _ in range(len(searchWord) - len(ans))]
        return ans


in_products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
in_search = "mouse"
a = Solution()
print(a.suggestedProducts(in_products, in_search))


"""

Add all the words in a trie then for every letter entered check for top 3 suggestions if their are, check 
alphabetically if you get end in the dict of the current word then add it to the suggestion till their are 3 suggestions 
or all the no other suggestions left for the entered letters 

Reference - https://leetcode.com/problems/search-suggestions-system/discuss/1660854/2-Clean-Python-OfficialSolution-(Self-Explained-Binary-Search-Trie)

Complexities:
Time -> O(chars in products)
Space -> O(chars in products)

"""
