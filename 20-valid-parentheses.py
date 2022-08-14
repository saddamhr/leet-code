class Solution:
    def isValid(self, s: str) -> bool:
        left_symbol = []
        for i in s:
            if i in ['(', '{', '[']:
                left_symbol.append(i)
            elif i == ')' and len(left_symbol) != 0 and left_symbol[-1] == '(':
                left_symbol.pop()
            elif i == '}' and len(left_symbol) != 0 and left_symbol[-1] == '{':
                left_symbol.pop()
            elif i == ']' and len(left_symbol) != 0 and left_symbol[-1] == '[':
                left_symbol.pop()
            else: return False
        return left_symbol == []

s = Solution()
p = "(]"
print(s.isValid(p))