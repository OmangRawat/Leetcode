"""

---> Letter Tile Possibilities
---> Medium

"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(output, curr_tiles):
            count = 0

            for i in range(len(curr_tiles)):
                if i == 0 or curr_tiles[i - 1] != curr_tiles[i]:
                    output.append(curr_tiles[i])
                    count += 1
                    count += backtrack(output, curr_tiles[:i] + curr_tiles[i + 1:])
                    output.pop()

            return count

        return backtrack([], sorted(tiles))


in_tiles = "AAABBC"
a = Solution()
print(a.numTilePossibilities(in_tiles))


"""
"""
