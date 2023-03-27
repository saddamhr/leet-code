from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        res = []
        for i in range(len(nums)):
            product = 1
            count += 1
            for j in range(len(nums)):
                
                print(i, j)
                if j+1 == len(nums):
                    break

                elif i != j:
                    product *= nums[j]
        
            res.append(product)
        return res
    
print(Solution().productExceptSelf([1,2,3,4]))