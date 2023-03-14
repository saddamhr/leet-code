'''
Solution: 01
Time Complexity: O(n)
Space Complexity: O(1)
'''


from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

print(Solution().fizzBuzz(15))

'''
Solution: 02
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0
            res = ''
            if divisibleBy3:res +='Fizz'
            if divisibleBy5:res +='Buzz'
            if not res:res =str(i)
            result.append(res)
        return result

print(Solution().fizzBuzz(15))
