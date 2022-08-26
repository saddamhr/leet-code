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
      return built_string

    def backspaceCompare(self, s: str, t: str) -> bool:
      final_s = self.build_string(s)
      final_t = self.build_string(t)

      if len(final_s) != len(final_t):
        return False
      else:
        for fs in range(len(final_s)):
          if final_s[fs] != final_t[fs]:
            return False
      return True



solution = Solution()

print(solution.backspaceCompare(s, t))