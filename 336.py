"""

---> Palindrome Pairs
---> Hard

"""
from collections import defaultdict
from functools import *


class Solution:
    def palindromePairs(self, words):
        word_dict = {word[::-1]: index for index, word in enumerate(words)}
        ans = []
        for index, word in enumerate(words):
            for char in range(len(word) + 1):
                prefix, suffix = word[:char], word[char:]
                if len(prefix) != 0 and prefix == prefix[::-1] and suffix in word_dict and word_dict[suffix] != index:
                    ans.append([word_dict[suffix], index])
                if suffix == suffix[::-1] and prefix in word_dict and word_dict[prefix] != index:
                    ans.append([index, word_dict[prefix]])
        return ans

    def palindromePairs_1(self, words):
        ans = set()
        word_dict = {words[x]: x for x in range(len(words))}
        for index, word in enumerate(words):
            reversed_word = word[::-1]
            length = len(word)
            for j in range(length + 1):
                if word[j:] == reversed_word[:length - j]:
                    if reversed_word[length - j:] in word_dict:
                        ans.add((index, word_dict[reversed_word[length - j:]]))
                if reversed_word[j:] == word[:length - j]:
                    if reversed_word[:j] in word_dict:
                        ans.add((word_dict[reversed_word[:j]], index))

        return [x for x in ans if x[0] != x[1]]

    def palindromePairs_wrong(self, words):
        def trie():
            return defaultdict(trie)

        def add_words(in_word, in_index):
            reduce(dict.__getitem__, in_word, word_dict)['end'] = in_index
            reduce(dict.__getitem__, reversed(in_word), reverse_dict)['end'] = in_index

        def get_total(in_dict):
            word2 = []
            for ind in in_dict.keys():
                if ind == 'end':
                    word2.append(in_dict['end'])
                else:
                    word2 += get_total(in_dict[ind])
            return word2

        word_dict = trie()
        reverse_dict = trie()
        ans = []
        for index, word in enumerate(words):
            add_words(word, index)

        for i, word in enumerate(words):
            if word == "":
                for j, w in enumerate(words):
                    if j != i and w == w[::-1]:
                        ans += [[i, j], [j, i]]
            else:
                curr_dict = reverse_dict
                index = 0
                for index, char in enumerate(word):
                    if char in curr_dict:
                        curr_dict = curr_dict[char]
                    else:
                        break
                # print(get_total(curr_dict))
                if index == len(word) - 1:
                    for j in get_total(curr_dict):
                        if j != i:
                            ans.append([i, j])

        return ans


in_words = ["a", "abc", "aba", ""]
# in_words = ["abcd", "dcba", "lls", "s", "sssll"]
a = Solution()
print(a.palindromePairs(in_words))


"""

Approach 1:
Store reverse of every string in a dictionary with its index
Divide each word into parts, 
either part1 should be palindrome and part2 should be available in the reversed dict keeping in check the index should 
not be same
else part2 should be palindrome and part1 should be available in the dictionary

Approach 2:
Store all words in a dict with their respective index
For every word reverse the word and check for any part if their first part is a palindrome sequence in it then search 
part2 of the word in dict
else check if the part2 of the string is palindromic and part1 is available in dict

"""
