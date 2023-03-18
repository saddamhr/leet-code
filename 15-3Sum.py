from typing import List
'''
Brute force approach
Time Complexity: O(n^3)
Space Complexity: O(n^2)
Status: TLE
'''

class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    if(nums[i] + nums[j] + nums[k] == 0):
                        result.append([nums[i], nums[j], nums[k]])
        return result
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))

'''
Two pointer approach
Time Complexity: O(n^2)
Space Complexity: O(n)
Status: TLE
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum  = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1 
                elif sum > 0:
                    right-=1
                else:
                    left+=1
        return result
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))