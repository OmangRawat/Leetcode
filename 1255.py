"""

---> Maximum Score Words Formed by Letters
---> Hard

"""
from collections import Counter
from functools import lru_cache


class Solution:
    def maxScoreWords(self, words, letters, score) -> int:
        @lru_cache(None)
        def dp(start, curr_letters):
            curr_letters = list(curr_letters)
            if start == n:
                return 0
            ans = dp(start + 1, tuple(curr_letters))
            temp = 0
            for c in words[start]:
                curr_letters[ord(c) - ord('a')] -= 1
                temp += score[c]
                if curr_letters[ord(c) - ord('a')] < 0:
                    return ans
            ans = max(ans, dp(start + 1, tuple(curr_letters)) + temp)
            return ans

        n = len(words)
        count = Counter(letters)
        letters = [0] * 26
        for key in sorted(count.keys()):
            letters[ord(key) - ord('a')] = count[key]
        score = {chr(ord('a') + i): val for i, val in enumerate(score)}
        return dp(0, tuple(letters))


in_words = ["dog", "cat", "dad", "good"]
in_letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
in_score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = Solution()
print(a.maxScoreWords(in_words, in_letters, in_score))
