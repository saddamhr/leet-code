class Solution(object):
    def intersection(self, nums1, nums2):
        res, d = [], {}

        for n in nums1:
            d[n] = 1
        
        for n in nums2:
            if n in d and d[n]:
                res.append(n)
                d[n] -= 1
        return res
            
print(Solution().intersection([1,2,2,1], [2,2])) # [2]