from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(word)
        return hashMap.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
