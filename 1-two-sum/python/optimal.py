from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            number_to_find = target - nums[i]

            if number_to_find in hash_map:
                # return [i, hash_map[number_to_find]]
                return [nums[i], nums[hash_map[number_to_find]]]
            hash_map[nums[i]] = i

s = Solution()

print(s.twoSum([2, 7, 11, 15], 9))
