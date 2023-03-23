class Solution:
    def isVowel(self, char):
        return True if char in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u') else False
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        left, right = 0, len(s_list)-1
        while left < right:
            if  self.isVowel(s_list[left]) and self.isVowel(s_list[right]):
                if s_list[left] != s_list[right]:
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                left+=1
                right-=1
            else:
                if not self.isVowel(s_list[left]): left+=1
                else: right -= 1
        s = ''.join(s_list)
        return s
            
# print(Solution().reverseVowels("hello"))
print(Solution().reverseVowels("leetcode")) #"leotcede"