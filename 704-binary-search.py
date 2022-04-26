from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        index = -1
        while(start <= end):
            mid = (start + end) // 2
            if target == nums[mid]:
                index = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            elif nums[end] > target: end = mid -1
        return index

s = Solution()
print(s.binary_search([-1,0,3,5,9,12], 9))