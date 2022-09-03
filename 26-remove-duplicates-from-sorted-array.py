from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        has_set = set()
        for n in nums:
            if n in has_set:
                continue
            else:
                has_set.add(n)
                nums.append(n)
        return nums
        # return len(has_set)
s = Solution()
print(s.removeDuplicates([1,1,2]))