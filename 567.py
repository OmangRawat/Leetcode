"""

---> Permutation in String
---> Medium

"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freq, a, match = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in char_freq:
                if not char_freq[s2[i]]:
                    match -= 1
                char_freq[s2[i]] -= 1
                if not char_freq[s2[i]]:
                    match += 1

            if i >= a and s2[i - a] in char_freq:
                if not char_freq[s2[i - a]]:
                    match -= 1
                char_freq[s2[i - a]] += 1
                if not char_freq[s2[i - a]]:
                    match += 1

            if match == len(char_freq):
                return True

        return False


in_s1 = "ab"
in_s2 = "eidbaooo"
a = Solution()
print(a.checkInclusion(in_s1, in_s2))


"""

Use counter to count no. of characters, check and reduce for each character increase the match which would return true 
when it reaches len of the required string

"""
