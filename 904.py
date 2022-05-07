"""

---> Fruit Into Baskets
---> Medium

"""


class Solution:
    def totalFruit(self, fruits) -> int:
        fruit_tracker = {}
        i = j = 0
        ans = 0
        for j, fruit in enumerate(fruits):
            if fruit not in fruit_tracker:
                fruit_tracker[fruit] = 1
            else:
                fruit_tracker[fruit] += 1

            while len(fruit_tracker) > 2 and i < j:
                fruit_tracker[fruits[i]] -= 1
                if not fruit_tracker[fruits[i]]:
                    fruit_tracker.pop(fruits[i], None)
                i += 1
            ans = max(ans, sum(fruit_tracker.values()))
            print(i, j, ans, fruit_tracker)
        return ans


in_fruits = [1, 0, 1, 4, 1, 4, 1, 2, 3]
a = Solution()
print(a.totalFruit(in_fruits))


"""

Track the starting indexes of the 2 fruits and the quantity of each fruit and remove the fruits of the a type whose 
index is lesser, change it with the new one

"""
