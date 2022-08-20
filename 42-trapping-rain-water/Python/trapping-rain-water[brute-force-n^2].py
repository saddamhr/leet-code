'''
    STATUS: Time Limit Exceeded
    Time Complexity: 0(n^2)
    Space Complexity: 0(1)
'''

from typing import List

heights = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2];

class Solution:
    def get_min_max(self, a, b, type) -> int:
        min_or_max_value = 0
        if type == 'min':
            min_or_max_value = a if a < b else b
        elif type == 'max':
            min_or_max_value = a if a > b else b
        return min_or_max_value

    def get_trapped_rain_water(self, height: List[int]) -> int:
        total_water = 0
        for p in range(len(height)):
            left_p = right_p = p
            max_left = max_right = 0

            # find left max value from current position
            while left_p >= 0:
                max_left = self.get_min_max(max_left, height[left_p], 'max')
                # max_left = max(max_left, height[left_p])
                left_p = left_p - 1

            # find right max value from current position
            while right_p < len(height):
                max_right = self.get_min_max(max_right, height[right_p], 'max')
                # max_right = max(max_right, height[right_p])
                right_p = right_p + 1

            # calculate water for current position
            current_water = min(max_left, max_right) - height[p]
            
            # calculate total water 
            if total_water >= 0:
                total_water = total_water + current_water

        return total_water

        
s = Solution()
# s.get_trapped_rain_water(heights)
print(s.get_trapped_rain_water(heights))