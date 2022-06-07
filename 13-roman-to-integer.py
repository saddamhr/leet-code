class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}
        sum = 0
        for index, i in enumerate(s):
            if i == 'M' and s[index-1] == 'C':
                if s == 'CM': dict_value = 800
                else: dict_value = 800
            elif i == 'C' and s[index-1] == 'X':
                if s == 'XC': dict_value = -10
                else: dict_value = 80
            elif i == 'V' and s[index-1] == 'I':
                if s == 'IV': dict_value = 3
                else: dict_value = 3
            elif i == 'X' and s[index-1] == 'I':
                if s == 'IX': dict_value = 8
                else: dict_value = -1
            elif i == 'L' and s[index-1] == 'X':
                if s == 'XL': dict_value = 30
                else: dict_value = 30
            elif i == 'D' and i == s[index-1] == 'C':
                if s == 'CD': dict_value = 900
                else: dict_value = 300 
            else:
                dict_value = dictionary.get(i)
            # print(dict_value)
            sum += dict_value
        return sum


s = Solution()
str = "IX"
print(s.romanToInt(str))
