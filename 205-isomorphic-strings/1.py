class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMapS, hashMapT = {}, {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if ((c1 in hashMapS and hashMapS[c1] != c2) or (c2 in hashMapT and hashMapT[c2] != c1)):
                    return False 
            hashMapS[c1] = c2
            hashMapT[c2] = c1
        return True
        
        
print(Solution().isIsomorphic("foo", "bar"))