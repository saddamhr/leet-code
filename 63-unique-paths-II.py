class Solution(object):
    def uniquePaths(self, obstacleGrid, m, n, memo):
        key = str(m) + ',' + str(n)
        if key in memo: return memo[key]
        if m < 0 or n < 0 or obstacleGrid[m][n] == 1: return 0
        if m == 0 and n == 0: return 1
        memo[key] = self.uniquePaths(obstacleGrid, m - 1, n, memo) + self.uniquePaths(obstacleGrid, m, n - 1, memo)
        return memo[key]


    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        memo = {}
        return self.uniquePaths(obstacleGrid, m, n, memo)
    





# print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])) # 2
# print(Solution().uniquePathsWithObstacles([[0,1],[0,0]])) # 1
# print(Solution().uniquePathsWithObstacles([[0,0],[0,1]])) # 1
# print(Solution().uniquePathsWithObstacles([[1,0],[0,0]])) # 1
# print(Solution().uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]])) # 7
print(Solution().uniquePathsWithObstacles([[0,1],[0,0]])) # 1
