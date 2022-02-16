"""

---> Reveal Cards In Increasing Order
---> Medium

"""
import collections


class Solution:
    def deckRevealedIncreasing(self, deck):
        d = []
        for x in sorted(deck)[::-1]:
            d = [x] + d[-1:] + d[:-1]
            print(d)
        return d

    def deckRevealedIncreasing_sol2(self, deck):
        ans = collections.deque()
        for x in sorted(deck)[::-1]:
            ans.rotate()
            ans.appendleft(x)
            print(ans)
        return list(ans)


in_deck = [17, 13, 11, 2, 3, 5, 7]
a = Solution()
# print(a.deckRevealedIncreasing(in_deck))
print(a.deckRevealedIncreasing_sol2(in_deck))


"""

Reference - https://leetcode.com/problems/reveal-cards-in-increasing-order/discuss/200515/JavaC%2B%2BPython-Simulate-the-Reversed-Process

Approach 1:
Add the next number ahead after keeping the last element of the list in first because it wll be shifted to last when
hand is shown

Complexities:
Time -> O(N^2)
Space -> O(N)


Approach 2:
when adding an element rotate the queue by one to right and add the element in left

Complexities:
Time -> O(NlogN)
Space -> O(N)

"""
