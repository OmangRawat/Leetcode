"""

---> Design Add and Search Words Data Structure
---> Medium

"""
from trie_func import trie_print
from collections import defaultdict
from functools import reduce


class WordDictionary:
    def __init__(self):
        def trie():
            return defaultdict(trie)
        self.word_dict = trie()

    def addWord(self, word: str) -> None:
        reduce(dict.__getitem__, word, self.word_dict)['end'] = 0
        # trie_print(self.word_dict)

    def search(self, word: str) -> bool:
        # curr_dict = self.word_dict
        def helper(curr_word, curr_dict):
            for index, char in enumerate(curr_word):
                if char == ".":
                    return any(helper(curr_word[index + 1:], curr_dict[x]) for x in curr_dict.keys() if curr_dict[x])
                elif char not in curr_dict:
                    return False
                else:
                    curr_dict = curr_dict[char]
            return True if "end" in curr_dict else False

        return helper(word, self.word_dict)


obj = WordDictionary()
obj.addWord("a")
in_add = [["ran"], ["rune"], ["runner"], ["runs"], ["add"], ["adds"], ["adder"], ["addee"]]
for i in in_add:
    obj.addWord(i[0])
# print(obj.word_dict)
trie_print(obj.word_dict)
in_search = [["r.n"], ["ru.n.e"], ["add"], ["add."], ["adde."], [".an."], ["...s"], ["....e."], ["......."], ["..n.r"]]
for i in in_search:
    print(obj.search(i[0]))


"""
Make a trie, add all words in it as they come
When searching if there is a . skip the char and check for their children else search for the char needed
"""
