"""

---> Coin Change
---> Medium

"""
import math


class Solution:
    def coinChange(self, coins, amount) -> int:
        # Memorization
        ans = {}
        coins = sorted(coins)

        def helper(amount_left):
            if amount_left == 0:
                return 0
            if amount_left not in ans:
                ans[amount_left] = math.inf
                for i in coins:
                    if i <= amount_left:
                        ans[amount_left] = min(ans[amount_left], helper(amount_left - i) + 1)
                # print(ans)
            return ans[amount_left]
        final = helper(amount)
        if final == math.inf:
            return -1
        return final

    def coinChange_sol2(self, coins, amount) -> int:
        # Tabulation
        n = len(coins)
        coins.sort()
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for amount_left in range(1, amount + 1):
            for coin in coins:
                if amount_left >= coin:
                    dp[amount_left] = min(dp[amount_left], dp[amount_left - coin] + 1)

        return dp[amount] if dp[amount] != math.inf else -1


in_coins = [2]
in_amount = 3
a = Solution()
print(a.coinChange(in_coins, in_amount))


"""

Keep track of amount - coins for each coin
Reference - https://leetcode.com/problems/coin-change/discuss/1475250/Python-4-solutions%3A-Top-down-DP-Bottom-up-DP-Space-O(amount)-Clean-and-Concise

Complexities:
Time -> max(O(N*amount), O(NlogN)) 
Space -> O(amount)

"""
