from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0   
                    digits.append(1)
                else:
                    digits[i] = 0
            else :
                digits[i]+=1
                return digits 
        return digits[::-1]

s = Solution()
print(s.plusOne([1,2,3]))
# print(s.plusOne([9,9]))