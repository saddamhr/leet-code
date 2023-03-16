'''
Solution 01: Bottom up dp approach
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one += two
            two = temp
        return one

print(Solution().climbStairs(5))



'''
Solution 02: Memoization dp approach
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution(object):
    def climbStairs(self, n, memo={}):
        if n in memo: return memo[n]
        if n == 1 or n == 2: return n
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return  memo[n]

print(Solution().climbStairs(44))

