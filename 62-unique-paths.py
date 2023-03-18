class Solution():
    def uniquePaths(self, m, n, memo={}):
        key = str(m) + ',' + str(n)
        if key in memo: return memo[key]
        if m == 0 or n == 0: return 0
        if m == 1 and n == 1: return 1
        memo[key] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m , n - 1, memo)
        return memo[key]
    
# print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(5, 4))