from typing import List

class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     hash_set = set()
        
    #     for i in nums:
    #         if not i in hash_set:
    #             hash_set.add(i)
    #         else:
    #             hash_set.remove(i)
    #     print(hash_set)
    #     return list(hash_set)[0]
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res
        
print(Solution().singleNumber([2,2,1]))