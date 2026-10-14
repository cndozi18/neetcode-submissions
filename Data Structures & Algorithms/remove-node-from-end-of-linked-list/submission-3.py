# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = l = r = head
        for i in range(n):
            r = r.next
        prev = None
        while r:
            prev = l
            l = l.next
            r = r.next
        if prev != None:
            prev.next = l.next
        else: 
            dummy.next = l.next
        return dummy.next

        