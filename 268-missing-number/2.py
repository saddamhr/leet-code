from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = (len(nums) + 1) * len(nums) // 2
        for i in range(len(nums)):
            # print(i)
            sum -= nums[i]
        return sum

print(Solution().missingNumber([3,0,1])) #2