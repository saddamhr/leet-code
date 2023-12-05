class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n // 2 != 0:
            div = n // 2
            res += div
            n = n - div
        return res

print(Solution().numberOfMatches(7))