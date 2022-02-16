from collections import defaultdict


def trie_print(trie):
    def helper(curr_trie):
        if type(curr_trie) != dict and not isinstance(curr_trie, defaultdict):
            return curr_trie

        ans = {}
        for i in curr_trie:
            ans[i] = helper(curr_trie[i])
        # print(ans)
        return ans

    print(helper(trie))
