class Solution(object):
    def findDifference(self, nums1, nums2):
        res1 = set()
        res2 = set()
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                res1.add(nums1[i])
            else: continue
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                res2.add(nums2[j])
            else: continue
        return [res1, res2]
print(Solution().findDifference([1,2,3], [2, 4, 6]))