from typing import List

class Solution:
    def is_alpha_neumeric(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        left ,right = 0, len(s) -1

        while left < right:
            while left < right and not self.is_alpha_neumeric(s[left]):
                left+=1
            while left < right and not self.is_alpha_neumeric(s[right]):
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right -1
        return True


        


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

