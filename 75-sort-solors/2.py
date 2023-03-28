from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            else:
                count2 += 1
        nums[:count0] = count0 * [0]
        nums[count0:count0 + count1] = count1 * [1]
        nums[count0+count1:] = count2 * [2]
        return nums
                