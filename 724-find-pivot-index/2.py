from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
        left_sum, right_sum = 0, total_sum
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1