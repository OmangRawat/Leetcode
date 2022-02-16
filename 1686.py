"""

---> Stone Game VI
---> Medium

"""


class Solution:
    def stoneGameVI(self, aliceValues, bobValues) -> int:
        alice_score = 0
        bob_score = 0
        chance = 0
        for v in sorted([i for i in range(len(aliceValues))], key=lambda z: -(aliceValues[z] + bobValues[z])):
            if chance == 0:
                alice_score += aliceValues[v]
                chance = 1
            else:
                bob_score += bobValues[v]
                chance = 0
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        return 0


in_alice = [2, 4, 3]
in_bob = [1, 6, 7]
a = Solution()
print(a.stoneGameVI(in_alice, in_bob))


"""

Sort the alice values in order according to the max difference that they can create if one person takes it and other 
doesn't that will create the best scenario for the person to win
Give one to alice then next to bob whoever has max sum at last wins

"""
