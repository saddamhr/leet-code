from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0
        prefixSum = {0 : 1}
        for i in range(len(nums)):
            current_sum += nums[i]
            diff = current_sum - k

            res += prefixSum.get(diff, 0)
            prefixSum[current_sum] = 1 + prefixSum.get(current_sum, 0)
        return res