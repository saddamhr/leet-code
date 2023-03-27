from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        if not hashMap:
            return -1
        else:
            print(hashMap)
            # return max(hashMap, key=hashMap.get)
            return min(hashMap.items(), key=lambda x: (-x[1], x[0]))[0]


# print(Solution().mostFrequentEven([0,1,2,2,4,4,1])) #2
# print(Solution().mostFrequentEven([4,4,4,9,2,4])) #2
# print(Solution().mostFrequentEven([29,47,21,41,13,37,25,7])) #2
print(Solution().mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290])) #2