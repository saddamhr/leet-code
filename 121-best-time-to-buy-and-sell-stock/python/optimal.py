'''
    STATUS: Time Limit Exceeded
    Time Complexity: 0(n)
    Space Complexity: 0(1)
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0  # 5

        while right < len(prices):
            if prices[left] < prices[right]:  # 1<4
                max_profit = max(max_profit, prices[right]-prices[left])
            else:
                left = right
            right += 1
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
