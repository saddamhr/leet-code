from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(len(matrix))
        probableArr = []
        for i in range(len(matrix)):
            print(matrix[i][-1])
            if matrix[i][-1] == target: return True
            elif matrix[i][-1] >= target:
                probableArr = matrix[i]
                break
        left, right = 0, len(probableArr) - 1
        while left <= right:
            mid = (left + right) // 2
            if probableArr[mid] == target: return True
            if probableArr[mid] < target:
                left = mid + 1
            else: right = mid -1
        return False