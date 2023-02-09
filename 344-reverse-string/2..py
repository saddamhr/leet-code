from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            print(l, r)
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

Solution().reverseString(["h","e","l","l","o"])
