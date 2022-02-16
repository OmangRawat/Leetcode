"""

---> Partition Array Into Three Parts With Equal Sum
---> Easy

"""


class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
        sum_of_part = sum(arr) / 3
        
        if sum_of_part != int(sum_of_part) or len(arr) < 3:
            return False
        
        curr_sum = 0
        no_of_parts = 0
        
        for i in arr:
            curr_sum += i
            print(curr_sum)
            
            if no_of_parts == 3:
                break
                
            if curr_sum == sum_of_part:
                curr_sum = 0
                no_of_parts += 1
                
        return no_of_parts == 3


in_arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
a = Solution()
print(a.canThreePartsEqualSum(in_arr))


"""
Check for each parts total sum then add till the sum is achieved then start sum for next part
"""
