"""

---> Divisor Game
---> Easy

"""


class Solution:
    def divisor_game(self, n: int) -> bool:
        dp = [False for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0 and (not dp[i - j]):
                    dp[i] = True
                    break
        return dp[n]

    def divisor_game_sol2(self, n: int) -> bool:
        return n % 2 == 0


in_n = 3
a = Solution()
print(a.divisor_game(in_n))
print(a.divisor_game_sol2(in_n))


"""
Approach1:
Bottom Up DP
dp[n] array denotes if the person gets number n then will he win or lose
Reference - https://leetcode.com/problems/divisor-game/discuss/274727/Python-DP

Complexities:
Time -> O(N^2)
Space -> O(N)

Approach2:
Odd no. have only odd divisors and odd - odd = even so the person who starts with even number wins
Reference - https://leetcode.com/problems/divisor-game/discuss/382233/Solution-in-Python-3-(With-Detailed-Proof)

Complexities:
Time -> O(1)
Space -> O(1)

"""
