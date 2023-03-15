from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            subArr = []
            sum = 0
            for j in range(1, i+1):
                if i <= 2:
                    subArr.append(1)
                else:
                    if j == 1:
                        subArr.append(1)
                    elif i == j:
                        subArr.append(1)
                    else:
                        val = result[i-2][j-1] + result[i-2][j-2]
                        subArr.append(val)
            result.append(subArr)
        return result

print(Solution().generate(3))
