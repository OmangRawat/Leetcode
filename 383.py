"""

---> Ransom Note
---> Easy

"""

r = "a"
m = "b"


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in range(len(magazine)):
            if magazine[i] not in letters:
                letters[str(magazine[i])] = 1
            else:
                letters[str(magazine[i])] += 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in letters:
                return 'false'
            elif letters[str(ransomNote[i])] == 0:
                return 'false'
            else:
                letters[str(ransomNote[i])] -= 1
        return 'true'


a = Solution()
print(a.canConstruct(r, m))


"""

List into a dictionary and check if all the words and amount needed is there

Complexities:
Time ->  O(M+N)
Space -> O(N)

"""
