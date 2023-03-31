from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = res = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        for i in range(len(nums) - 1):
            if nums[i] >= (nums[-1] - nums[i]):
                res += 1
        return res
                