"""

---> Best Sightseeing Pair
---> Medium

"""


def maxScoreSightseeingPair(a) -> int:
    max_so_far = a[0]
    result = 0
    for i in range(1, len(a)):
        result = max(result, max_so_far + a[i] - i)
        max_so_far = max(max_so_far, a[i] + i)
        # print(result)
        # print("-> ", max_so_far)
    return result


print(maxScoreSightseeingPair([8, 1, 5, 2, 6, 7]))

"""

---> Logic:

Divide the score in 2 parts i.e. a[i] + i and a[j] - j
Keep track of max of a[i] + i and max total score
Check for each upcoming a[j] - j to find max total score

Complexities:
Time -> O(N)
Space -> O(1)

"""
