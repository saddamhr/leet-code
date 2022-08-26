'''
    STATUS: Time Limit Exceeded
    Time Complexity: 0(n)
    Space Complexity: 0(1)
'''

from typing import List

heights = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2];

class Solution:
    def get_trapped_rain_water(self, height: List[int]) -> int:
        left = max_left = max_right = total_water = 0
        right = len(height) -1

        while left < right:
            if(height[left] <= height[right]):
                if height[left] >=  max_left:
                    max_left = height[left]
                else:
                    total_water = total_water + max_left - height[left]
                left = left +1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water = total_water + max_right - height[right]
                right = right - 1

        return total_water

        
s = Solution()
# s.get_trapped_rain_water(heights)
print(s.get_trapped_rain_water(heights))