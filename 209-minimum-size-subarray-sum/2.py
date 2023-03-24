'''
Status: Accepted
'''
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        numLen = len(nums) #6
        p1 = p2 = curr_sum = 0
        res = float('inf')
        while p2 < numLen:
            curr_sum += nums[p2]
            while curr_sum >= target:
                res = min(res, p2 - p1 + 1)
                curr_sum -= nums[p1]
                p1 += 1
        p2 += 1
        if res == float('inf'): return 0
        else: return res
# print(Solution().minSubArrayLen(7, [2,3,1,2,4,3])) # 1
# print(Solution().minSubArrayLen(4, [1,4,4]))
print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1])) #0