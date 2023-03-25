from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            local = local.split('+')[0].replace('.', '')
            res.add(f'{local}@{domain}')
        return len(res)