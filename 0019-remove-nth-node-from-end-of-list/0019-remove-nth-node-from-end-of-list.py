# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = end = head

        for _ in range(n):
            end = end.next
        
        while end and end.next:
            end = end.next
            cur = cur.next

        if not end:
            return head.next
        
        cur.next = cur.next.next
        return head