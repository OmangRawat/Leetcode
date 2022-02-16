"""

---> LRU Cache
---> Medium

"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache[key]
        self.cache.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


in_func = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
in_input = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
ans = []
for i, j in zip(in_func, in_input):
    if i == "LRUCache":
        obj = LRUCache(j[0])
        ans.append("null")
    elif i == "put":
        obj.put(j[0], j[1])
        ans.append("null")
    else:
        # print(obj.get(j[0]))
        ans.append(obj.get(j[0]))
        print(ans)


"""
Reference - https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList
"""
