class Solution:
    def firstUniqChar(self, s: str) -> int:
        sMap = {}
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)

        for i in range(len(s)):
            if s[i] in sMap and sMap.get(s[i]) == 1:
                return i
        return -1