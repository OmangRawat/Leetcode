"""

---> Restore IP Addresses
---> Medium

"""


class Solution:
    def restoreIpAddresses(self, s: str):
        def valid_integer(st):
            if len(st) == 0:
                return False
            elif st == "0":
                return True
            else:
                return st[0] != '0' and int(st) <= 255

        def backtrack(curr_s, subpart_length):
            if subpart_length > 3:
                return []
            elif subpart_length == 3:
                return [curr_s] if valid_integer(curr_s) else []
            else:
                ans = []
                for i in range(1, 4):
                    if valid_integer(curr_s[:i]):
                        print(curr_s[:i], backtrack(curr_s[i:], subpart_length + 1))
                        for r in backtrack(curr_s[i:], subpart_length + 1):
                            ans.append(curr_s[:i] + "." + r)
                return ans

        if len(s) <= 12:
            return backtrack(s, 0)
        else:
            return []


in_s = "101023"
# in_s = "255255255255"
a = Solution()
print(a.restoreIpAddresses(in_s))
