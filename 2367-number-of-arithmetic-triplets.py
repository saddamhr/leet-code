'''
Brute force approach
Time complexity: O(n^3)
Space complexity: O(1)
'''

from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplet = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if(nums[i] < nums[j] < nums[k] and nums[j] - nums[i] == diff  and nums[k] - nums[j] == diff):
                        triplet += 1
        return triplet
    
# print(Solution().arithmeticTriplets([4,5,6,7,8,9], 2))
print(Solution().arithmeticTriplets([4,5,6,7,8,9], 2))