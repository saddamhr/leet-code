from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
          print(i, nums[i])
          if i!= nums[i]:
            return i
        return i+1
       