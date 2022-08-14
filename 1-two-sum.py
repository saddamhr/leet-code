from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if dictionary.get(difference) is not None:
                return [dictionary.get(difference), i]
            else:
                dictionary[nums[i]] = i