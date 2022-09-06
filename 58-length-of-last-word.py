class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, i = len(s)-1, 0
        while s[length] == ' ':
            length-=1
        while length >= 0 and s[length] != ' ':
            i+=1
            length-=1
        return i


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))