"""

---> Most Frequent Subtree Sum
---> Medium

"""
from tree_func import *


class Solution:
    def findFrequentTreeSum(self, root):
        def dfs(curr_root):
            if not curr_root:
                return 0
            cur_root_sum = curr_root.value + dfs(curr_root.left) + dfs(curr_root.right)
            count[cur_root_sum] += 1
            return cur_root_sum
        count = defaultdict(int)
        dfs(root)
        max_freq = max(count.values())
        return [x for x in count if count[x] == max_freq]


in_array = [5, 2, -5]
in_root = to_binary_tree(in_array)
pretty_print(in_root)
a = Solution()
print(a.findFrequentTreeSum(in_root))


"""
Keep a default dict which keeps track of frequency of each sum, return sums with max freq

Complexities:
Time -> 
Space -> 

"""
