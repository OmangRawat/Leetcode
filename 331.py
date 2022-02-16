"""

---> Verify Preorder Serialization of a Binary Tree
---> Medium

"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        p = preorder.split(',')

        slot = 1
        for node in p:
            if slot == 0:
                return False

            if node == '#':
                slot -= 1
            else:
                slot += 1

        return slot == 0

    def isValidSerialization_sol2(self, preorder: str) -> bool:
        stack = []
        for elem in preorder.split(","):
            stack.append(elem)
            while len(stack) > 2 and stack[-2:] == ["#"] * 2 and stack[-3] != "#":
                stack.pop(-3)
                stack.pop(-2)
            print(stack)
        return stack == ["#"]


in_preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
a = Solution()
# print(a.isValidSerialization(in_preorder))
print(a.isValidSerialization_sol2(in_preorder))


"""
Reference - https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78564/The-simplest-python-solution-with-explanation-(no-stack-no-recursion)

Approach 1:

Everytime a number is there its +2 slots and -1 that it occupied and whenever # comes it is -1 slots as nothing can be
added after that

Approach 2:
For every "number # #" in string means no new element can be added in the tree below it so make it equal to # ans 
similarly reduce it till you reach elements less than 2 which should be # if its the right serialization 

"""
