from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted portion
            else:
                 if target < nums[mid] or target > nums[right]:
                     right = mid - 1
                 else:
                     left = mid + 1
        return -1
                

             

s = Solution()
print(s.search([3,4,5,6,1,2], 2))