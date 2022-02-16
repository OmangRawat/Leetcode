"""

---> Best Time to Buy and Sell Stock
---> Easy

"""


class Solution:
    def max_profit_sol_1(self, prices):
        n = len(prices)
        ans = 0
        min_val = prices[0]
        for i in range(1, n):
            ans = max(ans, prices[i] - min_val)
            min_val = min(min_val, prices[i])
        return ans

    # Kadane's Algorithm
    def max_profit_sol_2(self, prices):
        n = len(prices)
        ans = 0
        net = 0
        for i in range(n - 1):
            net += prices[i + 1] - prices[i]
            if net < 0:
                net = 0
            ans = max(ans, net)
        return ans


"""

Approach 1:
Keep the track of min value and max profit as you run through the loop

Approach 2:
Keep track of net change and compare with the max so far called Kadane's Algorithm

Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/263197/Python-2-solutions%3A-Min-So-Far-Kadane's-Algorithm-with-Picture-O(1)-in-Space

Complexities:
Time ->  O(N)
Space -> O(1)
(for both approaches)
"""
