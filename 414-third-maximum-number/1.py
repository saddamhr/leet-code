from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = nums[0]
        max2 = float('-inf')
        max3 = float('-inf')
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num < max1 and num > max2:
                max3 = max2
                max2 = num
            elif num < max2 and num > max3:
                max3 = num
        return max3 if max3 != float('-inf') else max1

