class Solution(object):
    def uniquePaths(self, grid, m, n, memo):
        key = str(m) + ',' + str(n)
        if key in memo: return memo[key]
        if m < 0 or n < 0: return float('inf')
        if m == 0 and n == 0: return grid[0][0]

        memo[key] = grid[m][n] + min(self.uniquePaths(grid, m - 1, n, memo), self.uniquePaths(grid, m , n - 1, memo))
        print(grid[m][n])
        return memo[key]

    def minPathSum(self, grid):
        m, n , memo = len(grid) - 1 , len(grid[0]) - 1, {}
        return self.uniquePaths(grid, m, n, memo)
    




print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # 7
