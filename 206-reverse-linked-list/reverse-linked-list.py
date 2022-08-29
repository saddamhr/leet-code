'''
    STATUS: Time Limit Exceeded
    Time Complexity: 0(n)
    Space Complexity: 0(1)
'''
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

print(Solution().reverseList([7,1,5,3,6,4]))