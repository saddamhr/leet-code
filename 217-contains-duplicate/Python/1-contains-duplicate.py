from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums = sorted(nums)
        for i in range(len(nums)-1):
            new_index = i +1
            if nums[new_index] == nums[new_index-1]:
                return True
        return False


s = Solution()
sorted_nums = sorted([1,1,1,3,3,4,3,2,4,2])
print(s.containsDuplicate(sorted_nums))
