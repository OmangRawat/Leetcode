"""

---> Evaluate Division
---> Medium

"""
from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        # DFS
        def get_value(num1, num2):
            seen.add(num1)
            out = 0
            for num in d[num1]:
                if num == num2:
                    return d[num1][num2]
                else:
                    if num not in seen:
                        out = d[num1][num] * get_value(num, num2)
                        if out != 0:
                            return out
            return 0

        d = defaultdict(dict)

        for i in range(len(equations)):
            n1, n2 = equations[i]
            v = values[i]
            d[n1][n2] = v
            d[n2][n1] = 1 / v

        print(d)

        ans = []

        for n1, n2 in queries:
            value = 0
            if n1 in d:
                seen = set()
                value = get_value(n1, n2)
                print(seen)
            if value:
                ans.append(value)
            else:
                ans.append(-1.0)
        return ans

    def calcEquation_sol2(self, equations, values, queries):
        all_values = defaultdict(dict)
        ans = []

        for i in range(len(equations)):
            n1, n2 = equations[i]
            cur_val = values[i]
            all_values[n1][n1] = 1
            all_values[n2][n2] = 1

            for key, val in all_values[n1].items():
                if key != n1:
                    all_values[key][n2] = all_values[key][n1] * cur_val
                    all_values[n2][key] = 1 / (all_values[key][n1] * cur_val)

            all_values[n1][n2] = cur_val
            all_values[n2][n1] = 1 / cur_val

            keys = list(all_values[n2].keys())
            for x in range(len(all_values[n2])):
                for y in range(x + 1, len(all_values[n2])):
                    all_values[keys[y]][keys[x]] = all_values[n2][keys[x]] / all_values[n2][keys[y]]
                    all_values[keys[x]][keys[y]] = all_values[n2][keys[y]] / all_values[n2][keys[x]]

        print(all_values)

        for i in queries:
            if i[0] in all_values and i[1] in all_values[i[0]]:
                ans.append(all_values[i[0]][i[1]])
            else:
                ans.append(-1.0)
        return ans


in_equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
in_values = [1.5, 2.5, 5.0]
in_queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
a = Solution()
# print(a.calcEquation(in_equations, in_values, in_queries))
print(a.calcEquation_sol2(in_equations, in_values, in_queries))


"""

Approach 1:
Make a dict of dict storing n1/n2 values using the equations
Now get the desired values by recursion
If the value is not already stored then divide n1/n2 into n1/num * num/n2 for nums in dict of n1
Reference - https://leetcode.com/problems/evaluate-division/discuss/1642378/Python-DFS-99.62-Simple

Approach 2:
Make a dict of dict storing equation values 
Use equations to get all the values that can be extracted from them
Reference - https://leetcode.com/problems/evaluate-division/discuss/1635330/Python-double-dict-union-find

"""
