'''
Status: TLE
'''
from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    def findAnagrams(self, s: str, p: str) -> List[int]:
        currentString = ""
        res =[]
        for i in range(len(s)):
            if len(currentString) == len(p):
                if(self.isAnagram(currentString, p)):
                    res.append(i-len(p))
                currentString = currentString[1:] +s[i]
            else:
                currentString+=s[i]
        if(self.isAnagram(currentString, p)):
            res.append(len(s)-len(p))
        return res
print(Solution().findAnagrams("abab", "ab"))