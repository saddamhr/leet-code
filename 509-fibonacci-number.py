'''
Solution 01: Classic recursion approach
Time Complexity: O(2^n)
Space complexity: O(n)
'''

class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return self.fib(n-1) + self.fib(n-2)

print(Solution().fib(2))

'''
Solution 02: Bottom up approach
Time Complexity: O(2^n)
Space complexity: O(n)
'''

class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1: return n
        one, two = 0, 1
        sum = 0
        for i in range(n-1):
            sum = one + two
            one = two
            two = sum
        return sum

print(Solution().fib(2))


'''
Solution 02: Memoization DP recursion approach
Time Complexity: O(2^n)
Space complexity: O(n)
'''

class Solution(object):
    def fib(self, n, memo={}):
        if n in memo: return memo[n]
        if n == 0 or n == 1: return n
        memo[n] = self.fib(n - 1, memo) + self.fib(n  - 2, memo)
        return memo[n]

print(Solution().fib(2))