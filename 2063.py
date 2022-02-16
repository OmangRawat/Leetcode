"""

---> Vowels of All Substrings
---> Medium

"""


class Solution:
    def count_vowels(self, word: str):
        counter = [0] * len(word)
        counter[0] = 1 if word[0] in "aeiou" else 0
        for i in range(1, len(word)):
            if word[i] in "aeiou":
                counter[i] = counter[i - 1] + (i + 1)
            else:
                counter[i] = counter[i - 1]
        return sum(counter)

    def count_vowels_sol2(self, word: str):
        return sum((i + 1) * (len(word) - i) for i, c in enumerate(word) if c in 'aeiou')


in_word = "noosabasboosa"
a = Solution()
print(a.count_vowels_sol2(in_word))


"""
A vowel will come once for every time till the place it is on and everytime for the letters after it
Reference - https://leetcode.com/problems/vowels-of-all-substrings/discuss/1563780/JavaC%2B%2BPython-Easy-and-Concise-O(n)

Complexities:
Time -> O(N)
Space -> O(N)

"""
