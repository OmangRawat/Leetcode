"""

---> Map Sum Pairs
---> Medium

"""


class MapSum:
    def __init__(self):
        self.keys_dict = {}

    def insert(self, key: str, val: int) -> None:
        if self.keys_dict.get(key, False):
            self.keys_dict[key] = val
        else:
            self.keys_dict.update({key: val})

    def sum(self, prefix: str) -> int:
        ans = 0
        for k in self.keys_dict.keys():
            if prefix == k[:len(prefix)]:
                ans += self.keys_dict[k]
        return ans


obj = MapSum()
obj.insert("apple", 3)
param_2 = obj.sum("ap")
print(param_2)
obj.insert("app", 2)
param_2 = obj.sum("ap")
print(param_2)


"""

Put all the elements as key value pair in a dictionary then check for the pattern in each word if you find it in the key 
just simply add the value into the sum

Reference - https://leetcode.com/problems/map-sum-pairs/discuss/1667592/93.15.-Python3-Easy-to-Understand

"""
