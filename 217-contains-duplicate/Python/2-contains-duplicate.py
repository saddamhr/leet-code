from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False


s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
