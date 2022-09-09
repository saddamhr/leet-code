from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(n)
        print(nums)

# print(Solution().moveZeroes([0,1,0,3,12]))
print(Solution().moveZeroes([0]))