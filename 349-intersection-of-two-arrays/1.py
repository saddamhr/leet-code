from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        hash_set = set()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]: i+=1
            elif nums1[i] > nums2[j]: j+=1
            else:
                hash_set.add(nums1[i])
                i+=1
                j+=1
        return list(hash_set)

        
        


        
print(Solution().intersection([1,2,2,1], [2,2])) # [2]
# print(Solution().intersection([4,9,5], [9,4,9,8,4])) # [4, 9]
# print(Solution().intersection([1], [1,1])) # [2]
# print(Solution().intersection([2, 1], [1,2])) # [2]