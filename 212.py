"""

---> Word Search II
---> Hard

"""
from collections import defaultdict
from functools import reduce


class Solution:
    def findWords(self, board, words):
        def trie():
            return defaultdict(trie)

        def addWord(word: str) -> None:
            reduce(dict.__getitem__, word, trie)['end', 'val'] = [True, word]

        def dfs(parent, m, n, x, y):
            ch = board[x][y]
            node = parent[ch]

            if 'end' in node:
                ans.append(node['val'])
                node['end'] = False
                # Don't RETURN since child.word can be a prefix of other words, e.g., 'ane' and 'aneis'

            board[x][y] = "#"
            for new_x, new_y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] in node:
                    dfs(node, m, n, new_x, new_y)
            board[x][y] = ch

            # hit the end of trie leaf node, if already checking "abcd" in trie leaf, (whether it works or not)
            # we don't need to spend time checking "abcde" word
            if not node:
                parent.pop(ch)

        trie = trie()

        for word in words:
            addWord(word)

        ans = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(trie, m, n, i, j)
        return ans


in_board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
in_words = ["oath", "pea", "eat", "rain"]
a = Solution()
print(a.findWords(in_board, in_words))
