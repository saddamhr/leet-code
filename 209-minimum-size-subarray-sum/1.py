'''
Status: TLE
'''
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        numLen = len(nums) #6
        p1 = p2 = 0
        res = float('inf')

        while p1 != numLen and p2 != numLen:
            if p1 == p2 and nums[p1] == target: return 1
            else:
                sum = 0
                for i in range(p1, p2+1):
                    sum += nums[i]
                if sum >= target:
                    print(res)
                    res = min(res, p2 - p1 + 1)
                    p1 += 1
                    p2 = p1
                elif sum < target:
                    p2 += 1
                elif sum > target:
                    p1 += 1
                    p2 = p1
        if res == float('inf'): return 0
        else: return res
# print(Solution().minSubArrayLen(7, [2,3,1,2,4,3])) # 1
# print(Solution().minSubArrayLen(4, [1,4,4]))
print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1])) #0