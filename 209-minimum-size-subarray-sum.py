from typing import List

class Solution:
    def minSubArrayLen(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        length = 0
        # index = -1
        # sum = 0
        while(start <= end):
            sum = 0
            mid = (start + end) // 2
            if target == nums[mid]:
                length = 1
                # index = mid
                break
            elif nums[mid] < target:
                start = mid + 1
                sub_arr = nums[start:end+1]
                print('sub arr-->',sub_arr)
                for i in sub_arr:
                    sum += i
                print('sum1-->', sum)
                if sum == target:
                    length = len(sub_arr)
                    break
            elif nums[end] > target:
                end = mid - 1
                sub_arr = nums[start] + nums[end]
                for i in sub_arr:
                    sum += i
                print('sum2-->', sum)
                if sum == target:
                    length = len(sub_arr)
                    break
        return length
        # sub_arr = nums[start] + nums[end]
        # for i in sub_arr:
        #     sum += i
        # if sum == target:
        #     return len(sub_arr)
        # else:
        #     return 0


s = Solution()
sorted_arr = sorted([2, 3, 1, 2, 4, 3])
# print(sorted_arr)
print(s.minSubArrayLen(sorted_arr, 7))
