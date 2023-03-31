class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1: return True
        return False
    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output