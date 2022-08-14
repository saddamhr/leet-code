# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        m = []
        i=j=k=0
        n = len(list1)
        m = len(list2)
        while i<n and j<m:
            if list1[i] > list2[j]:
                m[k] = list2[j]
                j+=1
            else:
                m[k] = list1[i]
                i+=1
            k+=1
        
        
        while i<n:
            m[k] = list1[i]
            i+=1
            k+=1
        
        
        while j<m:
            m[k] = list1[j]
            j+=1
            k+=1
        