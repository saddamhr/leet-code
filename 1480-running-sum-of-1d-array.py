'''
Solution 1
Time Complexity: O(n)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum 
        return nums


s = Solution()
print(s.runningSum([1,2,3,4]))

'''
Solution 2
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] 
        return nums


s = Solution()
print(s.runningSum([1,2,3,4]))