from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res, left, right = nums[0], 0, len(nums) - 1

        while left <= right:
            if nums [left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res

