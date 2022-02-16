"""

---> Backspace String Compare
---> Easy

"""
import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_str(string):
            hash_counter = 0
            for char in reversed(string):
                if char == '#':
                    hash_counter += 1
                elif hash_counter:
                    hash_counter -= 1
                else:
                    yield char
                print(string, char, hash_counter)

        final_s, final_t = final_str(s), final_str(t)
        # print(final_s, final_t)
        for i, j in itertools.zip_longest(final_s, final_t):
            if i != j:
                return False
        return True


in_s = "ac"
in_t = "ac"
a = Solution()
print(a.backspaceCompare(in_s, in_t))


"""
Reference - https://leetcode.com/problems/backspace-string-compare/discuss/449528/844-Backspace-String-Compare-Py-All-in-One-By-Talse
Approach 1:
Use simple stack and push chars pop last one if # comes and compare strings at last

Complexities:
Time -> O(M+N)
Space -> O(N)

Approach 2:
Use a function to get final string by using yield which sends value back without storing it in memory unlike return
Use yield when u need to return multiple values rather than return

Complexities:
Time -> O(M+N)
Space -> O(1)

"""
