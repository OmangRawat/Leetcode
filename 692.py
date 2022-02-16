"""

---> Top K Frequent Words
---> Medium

"""
from collections import Counter
from heapq import *



class Solution:
    def topKFrequent(self, words, k: int):
        word_count = Counter(words)
        heap, ans = [], []
        for key in word_count:
            heappush(heap, (-word_count[key], key))
        for i in range(k):
            count, word = heappop(heap)
            ans.append(word)
        return ans


in_words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
in_k = 4
a = Solution()
print(a.topKFrequent(in_words, in_k))


"""
Keep a counter of all words then push them into a minh heap with negative of frequency and pop top k elements
"""
