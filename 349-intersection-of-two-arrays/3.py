class Solution(object):
    def intersection(self, nums1, nums2):
        result = set()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    result.add(nums1[i])
                    break
        return list(result)
print(Solution().intersection([1,2,2,1], [2,2])) # [2]