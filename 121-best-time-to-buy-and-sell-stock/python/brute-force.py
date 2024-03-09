'''
    STATUS: Time Limit Exceeded
    Time Complexity: 0(n^2)
    Space Complexity: 0(1)
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_max = 0

        for i in range(len(prices)):
            local_max = prices[i]
            for j in range(i + 1, len(prices)):
                local_max = max(local_max, prices[j])
            global_max = max(global_max, local_max - prices[i])
        return global_max
