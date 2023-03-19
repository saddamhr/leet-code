from typing import List
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


'''
Two pointer approach
Time Complexity: O(n^2)
Space Complexity: O(n)
Status: Accepted
'''

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplet = 0
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                if nums[i] < nums[left] < nums[right] and nums[left] - nums[i] == diff  and nums[right] - nums[left] == diff:
                    triplet += 1
                    left+=1
                elif nums[right] - nums[left] > diff and nums[right] > nums[left]:
                    right-=1
                else:
                    left+=1
        return triplet
    
print(Solution().arithmeticTriplets([0,1,4,6,7,10], 3))