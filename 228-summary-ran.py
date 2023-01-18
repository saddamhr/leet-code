from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start_index, result = 0, []

        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] +1 == nums[i+1]:
                continue
            if start_index == i:
                result.append(str(nums[start_index]))
            else:
                result.append(str(nums[start_index])+"->"+str(nums[i]))
            start_index = i + 1
        return result


s = Solution()
sorted_arr = [0,2,3,4,6,8,9] #["0", "2->4", "6", "8->9"]
s.summaryRanges(sorted_arr)