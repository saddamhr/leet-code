class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = {}
        for i in range(len(magazine)):
            magDict[magazine[i]] = 1 + magDict.get(magazine[i], 0)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magDict or magDict.get(ransomNote[i]) <= 0:
                return False
            magDict[ransomNote[i]] = magDict.get(ransomNote[i]) -1 
        return True

# print(Solution().canConstruct("aa", "aab")) #True
# print(Solution().canConstruct("aa", "ab")) #False
print(Solution().canConstruct("a", "b")) #False