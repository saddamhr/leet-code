from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        mid = len(nums)//2
        if len(nums) % 2 == 0:
            return  (nums[mid] + nums[mid - 1]) / 2
        else:
            return nums[mid]

print(Solution().findMedianSortedArrays([1,3], [2]))