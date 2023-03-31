
from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left, right, res = 0, sum(nums), 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                res += 1
        return res