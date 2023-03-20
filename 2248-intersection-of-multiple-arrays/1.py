class Solution(object):
    def intersection(self, nums):
        dictionary = {}
        length = len(nums)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                key = str(nums[i][j]) 
                if key in dictionary: dictionary[key] = dictionary.get(key)+1
                else: dictionary[key] = 1
        nums = []
        for key, value in dictionary.items():
            if value == length:
                nums.append(int(key))
        return sorted(nums)

    
print(Solution().intersection([[7,34,45,10,12,27,13],[27,21,45,10,12,13]])) #[10,12,13,27,45]
