from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        row, cols = len(matrix), len(matrix[0])
        left, right = 0, row * cols - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // cols][mid % cols]
            if num == target: return True
            elif num < target: left = mid + 1
            else: right = mid - 1
        return False