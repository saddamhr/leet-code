s = 'ab#c'
t = 'ad#c'

class Solution:
    def build_string(self,string):
      built_string = []
      for s in string:
        if s != '#':
          built_string.append(s)
        elif built_string:
          built_string.pop()
      return built_string.join('')

    def backspaceCompare(self, s: str, t: str) -> bool:
      final_s = self.build_string(s)
      final_t = self.build_string(t)

      return final_s == final_t



solution = Solution()

print(solution.backspaceCompare(s, t))