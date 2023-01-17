from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        row1, row2, row3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm') 
        for w in words:
            word_c = set(w.lower())
            if word_c<=row1 or word_c <= row2 or word_c <= row3:
                res.append(w)
        return res


words = ["Hello","Alaska","Dad","Peace"]
s = Solution()
print(s.findWords(words))