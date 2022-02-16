"""

---> Find and Replace Pattern
---> Medium

"""


class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        ans = []
        pattern_len = len(pattern)
        for word in words:
            if len(word) != pattern_len:
                continue

            curr_word = ''
            pattern_tracker = {pattern[0]: word[0]}
            for i in range(pattern_len):
                if pattern[i] in pattern_tracker:
                    curr_word += pattern_tracker[pattern[i]]
                else:
                    if word[i] in pattern_tracker.values():
                        break
                    pattern_tracker[pattern[i]] = word[i]
                    curr_word += pattern_tracker[pattern[i]]
            if curr_word == word:
                ans.append(word)
        return ans


in_words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
in_pattern = "abb"
a = Solution()
print(a.findAndReplacePattern(in_words, in_pattern))
