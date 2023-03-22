class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxLen = 0
        chars = set()
        while right < len(s):
            if  s[right] not in chars:
                chars.add(s[right])
                right += 1
                maxLen = max(maxLen, len(chars))
            else:
                chars.remove(s[left])
                left+=1
        return maxLen
print(Solution().lengthOfLongestSubstring("abcabcbb")) #3
# print(Solution().lengthOfLongestSubstring("au")) #2
# print(Solution().lengthOfLongestSubstring("dvdf")) #3