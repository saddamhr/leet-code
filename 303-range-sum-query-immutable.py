'''
Solution: 01
'''
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums.insert(0,0)
        self.prefixSum = [0]
        for i in range(len(nums)):
            self.prefixSum.append(nums[i]+self.prefixSum[i])
        print(self.prefixSum)

    def sumRange(self, left, right):
        print(self.nums)
        return self.prefixSum[right+1] -self.prefixSum[left]
   
obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(0,2)

'''
Solution: 02
'''
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.nums.insert(0,0)
        for i in range(1, len(nums)):
            self.nums[i]+=self.nums[i-1]

    def sumRange(self, left, right):
        return self.nums[right+1] -self.nums[left]

    
obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(0,2)