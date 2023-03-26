from typing import List
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        res = []
        for i in range(k):
            key=lambda k: hashMap[k]
            print(key)
            max_key = max(hashMap, key=lambda k: hashMap[k])
            res.append(max_key)
            del hashMap[max_key]
        if len(res) == 0: return nums
        else: return res
# print(Solution().topKFrequent([1,2], 2))
print(Solution().topKFrequent([1,1,1,2,2,3], 2))