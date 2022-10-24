
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''

        while columnNumber > 0:
            c = chr(ord('A') + (columnNumber -1) % 26)
            print(c)
            result = c + result
            columnNumber = (columnNumber-1)//26
        return result


s = Solution()
print(s.convertToTitle(701))