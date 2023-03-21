import math
class Solution(object):
    def zeroFilledSubarray(self, nums):
        nums.append(-1)
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0: count += 1
            else:
                res += count * (count + 1) // 2
                count = 0

        return res
        
# print(Solution().zeroFilledSubarray([1,3,0,0,2,0,0,4])) #6
print(Solution().zeroFilledSubarray([0,0,0,2,0,0])) #9