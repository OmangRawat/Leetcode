"""

---> 24 Game
---> Hard

"""
from itertools import permutations


class Solution:
    def judgePoint24(self, cards) -> bool:
        def calculate(curr_cards):
            if len(curr_cards) <= 1:
                return curr_cards
            else:
                values = set()
                for split_point in range(1, len(curr_cards)):
                    for left_val in calculate(curr_cards[:split_point]):
                        for right_val in calculate(curr_cards[split_point:]):
                            values.add(left_val + right_val)
                            values.add(left_val - right_val)
                            values.add(left_val * right_val)
                            if right_val != 0:
                                values.add(left_val / right_val)
                return values

        for permutation in permutations(cards):
            for c in calculate(permutation):
                if 23.99 < c < 24.01:
                    return True

        return False


in_cards = [4, 1, 8, 7]
a = Solution()
print(a.judgePoint24(in_cards))
