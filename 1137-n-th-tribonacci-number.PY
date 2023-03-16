'''
Solution 01: Bottom up dp approach
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution(object):
    def tribonacci(self, n):
        if n == 1: return n
        one, two , three = 0, 0, 1
        sum = 0
        for i in range(n-1):
            sum = one + two + three
            one = two
            two = three
            three = sum
        return sum

print(Solution().tribonacci(25))

'''
Solution 02: Memoization dp approach
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution(object):
    def tribonacci(self, n, memo={}):
        if n in memo: return memo[n]
        if n == 0:
                return  0
        if n ==1 or n ==2:
            return 1            
        memo[n] = self.tribonacci(n-1, memo) + self.tribonacci(n-2, memo) + self.tribonacci(n-3, memo)        

        return memo[n]