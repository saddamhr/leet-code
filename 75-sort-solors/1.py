from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        mid = 0
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        return nums