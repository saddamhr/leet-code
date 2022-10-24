
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0 # 1
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            print(i)
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0 # 0 < 2, 1
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0 # 0 < 1, 1

            total = digitA + digitB + carry # 2
            char = str(total % 2) # 0
            res = char + res
            carry = total // 2 #1, 
        if carry:
            res = '1' + res
        return res

s = Solution()
print(s.addBinary('11', '1'))