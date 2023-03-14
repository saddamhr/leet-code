from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            sum = 0
            for wealth in account:
                sum+=wealth
                maxWealth = max(maxWealth, sum)
        return maxWealth



# print(Solution().maximumWealth([[1,2,3],[3,2,1]]))
print(Solution().maximumWealth([[1,5],[7,3],[3,5]]))