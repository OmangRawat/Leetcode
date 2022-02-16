"""

---> Dota2 Senate
---> Medium

"""
import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        dire = collections.deque()
        radiant = collections.deque()
        for i, c in enumerate(senate):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"

    def predictPartyVictory_sol2(self, senate: str) -> str:
        persons = senate
        people = collections.Counter(senate)
        bans = {"R": 0, "D": 0}

        while "R" in persons and "D" in persons:
            person = persons[0]
            persons = persons[1:]
            if bans[person]:
                bans[person] -= 1
                people[person] -= 1
            else:
                if person == "R":
                    bans["D"] += 1
                else:
                    bans["R"] += 1
                persons += person
            print(people)

        return "Radiant" if "R" in persons else "Dire"


in_senate = "RDRDRDDR"
a = Solution()
# print(a.predictPartyVictory(in_senate))
print(a.predictPartyVictory_sol2(in_senate))


"""

Approach 1:
Take 2 queues for putting in indexes of the Radicals and Dire, Pop out indexes, compare and larger one is discarded and
other put back to array which will have chance after total people + his index
Reference - https://leetcode.com/problems/dota2-senate/discuss/399786/Python-with-two-queues

Complexities:
Time -> O(N)
Space -> O(N)


Approach 2:
keep track of no. of persons remaining and no. of bans left on that group

Complexities:
Time -> O(N)
Space -> O(1)

"""
