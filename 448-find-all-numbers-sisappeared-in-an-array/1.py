from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_number_set = set(range(1, len(nums)+1))

        for num in nums:
            if num in all_number_set:
                all_number_set.remove(num)
        return list(all_number_set)

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))