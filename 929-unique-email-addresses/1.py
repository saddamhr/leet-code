from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for i in range(len(emails)):
            validPartPlus = emails[i].split('+')
            ignoreDot = ''
            if len(validPartPlus) == 1:
                validPartPlus = emails[i].split('@')
                validPartDot = ''.join(validPartPlus[0]).split('.')
                for j in range(len(validPartDot)):
                    ignoreDot += validPartDot[j]
            else:
                validPartDot = ''.join(validPartPlus[0]).split('.')
                for j in range(len(validPartDot)):
                    ignoreDot += validPartDot[j]
            res.add(ignoreDot + '@' + emails[i].split('@')[-1])
        return len(res)
    
print(Solution().numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"])) #1