"""

---> Best Time to Buy and Sell Stock II
---> Medium

"""


class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i, price in enumerate(prices[1:], start=1):
            if prices[i - 1] < price:
                profit += price - prices[i - 1]
        return profit


in_prices = [7, 1, 5, 3, 6, 4]
a = Solution()
print(a.maxProfit(in_prices))


"""
Check for profit between every simultaneous nodes and take their sum and skip the non-profit ones that will give maximum 
profit
"""
