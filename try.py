from collections import defaultdict
from functools import reduce
from trie_func import trie_print


def trie():
    return defaultdict(trie)


word_dict = trie()
ans = []
words = ["me", "time", "bell"]

# for i in words:
#     a = reduce(dict.__getitem__, i[::-1], word_dict)
#     ans.append(a)
#     print("____________________________")
#     trie_print(a)
#     for j in ans:
#         print("*********")
#         print(i)
#         trie_print(j)

a = reduce(dict.__getitem__, "me"[::-1], word_dict)
trie_print(a)
b = reduce(dict.__getitem__, "time"[::-1], word_dict)[:]
c = reduce(dict.__getitem__, "bell"[::-1], word_dict)[:]
trie_print(a)

trie_print(word_dict)
for i in ans:
    print(i)
    trie_print(i)

# x = [[1], [2], [3], [4], [5]]
# ans = []
# y = [reduce(dict.__getitem__, i, ans) for i in x]
# print(y)
