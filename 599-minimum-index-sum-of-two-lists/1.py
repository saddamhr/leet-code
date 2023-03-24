from typing import List
import sys
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashMap = {}
        m = len(list1)
        n = len(list2)

        for i in range(m):
            hashMap[list1[i]] = i
        ans = []
        minIndex = sys.maxsize
        for i in range(n):
            if list2[i] in hashMap:
                currentIndex = i + hashMap[list2[i]]
                if currentIndex < minIndex:
                    ans.clear()
                    minIndex = currentIndex
                    ans.append(list2[i])
                elif currentIndex == minIndex:
                    ans.append(list2[i])
        return ans
        