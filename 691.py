"""

---> Stickers to Spell Word
---> Hard

"""
from collections import Counter
from functools import lru_cache


class Solution:
    def minStickers(self, stickers, target: str) -> int:
        @lru_cache(None)
        def dp(s):
            if s == '':
                return 0

            letter_count = Counter(s)
            min_stickers = float('inf')

            for sticker in stickers:
                if s[0] not in sticker:
                    continue
                min_stickers = min(min_stickers, 1 + dp(''.join(char * char_count for char, char_count in sorted((letter_count - sticker).items()))))
            return min_stickers

        n = len(stickers)
        stickers = [Counter(sticker) for sticker in stickers]
        ans = dp(''.join(sorted(target)))
        return -1 if ans == float('inf') else ans


in_sticker = ["with", "example", "science"]
in_target = "thehat"
a = Solution()
print(a.minStickers(in_sticker, in_target))
